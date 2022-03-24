import json
import re

import pandas as pd
import numpy as np

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
    def __init__(self):
        """
        Constructor for the model
        """
        self.data_ = None  # data that the model uses to train on
        self.model_ = None  # model that takes in user input and outputs intent
        self.label_map_ = None  # maps output to label
        self.responses_ = None  # maps label to list of responses
        self.tokenizer_ = None  # tokenizer used to change strings to vectors with numbers

        self.__load_data()
        self.__create_model()

    def __str__(self):
        """
        String conversion of model
        """
        return self.model_.summary()

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

    def __load_data(self):
        """
        loads in the data from the intents file,
        and returns a pandas data frame and sets the data and label_map members
        """
        with open('data/obiwanintents.json') as file:
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

        # shuffle the data
        data = data.sample(frac=1).reset_index(drop=True)

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
        return X

    def __create_model(self, embedding_dim=64):
        """
        Creates the model
        :param embedding_dim: number of dimensions for embedding layer
        """
        X = self.__tokenize_initial_data()

        # get input shape from teh tokenized data
        # shape can change with changes in the data so this is the best way for future proofing the model
        input_shape = X.shape[1]

        inputs = keras.Input(input_shape, name='input')

        # embedding layer to create a feature map of the initial vector
        lyr = keras.layers.Embedding(input_dim=len(self.tokenizer_.word_index) + 1, output_dim=embedding_dim,
                                     name='embedding')(inputs)

        # LSTM layer is the best way to understand NLP,
        # due to its memory components that allow it to understand sequences
        lyr = keras.layers.LSTM(embedding_dim, return_sequences=True, name='lstm')(lyr)

        # flatten to 1D so it's easier on the dense layer
        lyr = keras.layers.Flatten(name='flatten')(lyr)

        # use softmax activation since all the labels are mutually exclusive
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

