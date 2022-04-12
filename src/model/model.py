import json
import re
import random

import pandas as pd

import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


class Model:
    """
    This class houses the text classification model for the chatbot
    """

    #
    # CONSTRUCTORS
    #
    def __init__(self, data_path='../data/obiwanintents.json'):
        """
        Constructor for the model
        """
        self.data_path_ = data_path  # path where data is located
        self.data_ = None  # data that the model uses to train on
        self.label_map_ = None  # maps output to label
        self.responses_ = None  # maps label to list of responses

        self.tokenizer_ = None  # tokenizer used to change a string to a vector with numbers
        self.input_shape_ = None  # shape of the input, needed for padding user inputs

        self.model_ = None  # model that takes in user input and outputs intent

        self.__load_data(data_path)  # initializes: data_ label_map_ responses_
        self.__tokenize_initial_data()  # initializes: tokenizer: input_shape_
        self.__create_model()  # initializes: model_

    def __str__(self):
        """
        String conversion of model
        """
        self.model_.summary()
        return ''

    #
    # PRIVATE FUNCTIONS
    #
    def __standardize_text(self, string):
        """
        Makes string lower case and removes punctuation
        :param string: string to be converted
        :return: converted string
        """
        return re.sub(r'[^\w\s]', '', string).lower()

    def __load_data(self, name):
        """
        loads in the data from the intents file,
        and returns a pandas data frame and sets the data and label_map members
        :param name: name of the file to load
        """
        with open(name) as file:
            data = json.load(file)

        # parse through data
        responses = {}
        inputs = []
        labels = []
        label_map = {}

        count = 0
        for intent in data['intents']:
            responses[intent['tag']] = intent['responses']
            label_map[intent['tag']] = count
            count += 1
            for message in intent['inputs']:
                inputs.append(message)
                labels.append(intent['tag'])

        # store responses
        self.responses_ = responses

        # converting to dataframe
        data = pd.DataFrame({"inputs": inputs,
                             "labels": labels})

        data['labels'].replace(label_map, inplace=True)

        # standardize all text to be lowercase and no punctuation
        for i in range(len(data)):
            data['inputs'].iloc[i] = self.__standardize_text(data['inputs'].iloc[i])

        # reverse the label map so each number is the key
        # this needs to be reversed since output of model is the number
        self.label_map_ = dict((v, k) for k, v in label_map.items())
        self.data_ = data

    def __tokenize_initial_data(self):
        """
        Uses the training data to fit a tokenizer
        :return: tokenized data
        """
        # allow up to 10000 unique words
        self.tokenizer_ = Tokenizer(num_words=10000)
        self.tokenizer_.fit_on_texts(self.data_['inputs'])
        X = self.tokenizer_.texts_to_sequences(self.data_['inputs'])
        X = pad_sequences(X)

        # get input shape from the tokenized data
        # shape can change with changes in the data so this is the best way for future proofing the model
        self.input_shape_ = X.shape[1]

        return X

    def __create_model(self, embedding_dim=64):
        """
        Creates the model
        :param embedding_dim: number of dimensions for embedding layer
        """

        # MODEL ARCHITECTURE:
        #
        # embedding layer to create a feature map of the initial vector
        #
        # LSTM layer is the best way to understand NLP,
        # due to its memory components that allow it to understand sequences
        #
        # flatten to 1D so that it's easier on the dense layer
        #
        # use softmax activation since all the labels are mutually exclusive
        inputs = keras.Input(self.input_shape_, name='input')

        lyr = keras.layers.Embedding(input_dim=len(self.tokenizer_.word_index) + 1, output_dim=embedding_dim,
                                     name='embedding')(inputs)
        lyr = keras.layers.LSTM(embedding_dim, name='lstm')(lyr)
        lyr = keras.layers.Flatten(name='flatten')(lyr)
        outputs = keras.layers.Dense(13, activation='softmax', name='output')(lyr)

        self.model_ = keras.Model(inputs=inputs, outputs=outputs, name='ObiWan_Kenobot')

        # compiling the model
        # sparse categorical cross entropy loss since each category is mutually exclusive
        self.model_.compile(loss="sparse_categorical_crossentropy",
                            optimizer='adam', metrics=['accuracy'])

    #
    # PUBLIC FUNCTIONS
    #
    def summary(self):
        """
        returns the summary of the model
        :return: summary of the model
        """
        return self.model_.summary()

    def train(self):
        """
        Trains the model on the given data
        :return: history of losses and metrics
        """
        X = self.__tokenize_initial_data()
        return self.model_.fit(X, self.data_['labels'],
                               epochs=10000,
                               callbacks=[tf.keras.callbacks.EarlyStopping(patience=5, monitor='loss')])

    def save_model(self, name="model"):
        """
        saves the weights to a .ckpt file with the given name to the directory saved_models
        :param name: name of the file
        """
        self.model_.save_weights('saved_models/'+name)

    def load_model(self, path='saved_models/model'):
        """
        loads the weights from the file with the given name
        :param path: path to the file to load in
        """
        self.model_.load_weights(path)
        self.model_.compile(loss="sparse_categorical_crossentropy",
                            optimizer='adam', metrics=['accuracy'])

    def chat(self, user_input):
        """
        Accepts a string input from the user and returns a response that corresponds to the predicted intent
        :param user_input: string that the user sends the bot
        :return: string that the bot responds with
        """
        # vectorize input to be able to use in the model
        user_input = self.__standardize_text(user_input)
        vec = self.tokenizer_.texts_to_sequences([user_input])
        vec = [item for i in vec for item in i]  # needs to be flattened for padding
        vec = pad_sequences([vec], self.input_shape_)

        # get label
        label = self.model_.predict(vec)
        label = label.argmax()
        tag = self.label_map_[label]

        # return a random corresponding response
        responses = self.responses_[tag]
        i = random.randint(0, len(responses)-1)
        return responses[i]

    def test(self):
        """
        Used to test the accuracy of the model
        """
        greeting = ['how are you', 'greeting']
        goodbye = ['See you later.', 'goodbye']
        thanks = ['Thank you so much!', 'thanks']
        tasks = ['What can you do?', 'tasks']
        alive = ['Are you even alive at all?', 'alive']
        hlp = ['PLease I need your help!', 'help']
        mission = ['Can you tell me a little bit about your mission?', 'mission']
        jedi = ['are you a jedi?', 'jedi']
        sith = ['Who is the most evil sith in the galaxy?', 'sith']
        bounty = ['Do you know of Jango Fett?', 'bounty hunter']
        funny = ['I know you know some good jokes', 'funny']
        stories = ['Cmon, tell me a story!', 'stories']
        threat = ['I will fight you', 'threat']

        messages = [greeting, goodbye, thanks, tasks, alive, hlp, mission, jedi, sith, bounty, funny, stories, threat]

        correct = 0
        for msg in messages:
            msg[0] = self.__standardize_text(msg[0])
            X = self.tokenizer_.texts_to_sequences([msg[0]])
            X = [item for i in X for item in i]
            X = pad_sequences([X], self.input_shape_)
            pred = self.model_.predict(X)
            pred = pred.argmax()
            print('Pred: {} Actual: {}'.format(self.label_map_[pred], msg[1]))
            if self.label_map_[pred] == msg[1]:
                correct += 1
            print()

        accuracy = correct / len(messages)
        print('Accuracy = {:.2f}'.format(accuracy))
