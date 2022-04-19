# Version 2.3.1
* Changed command prefix to ob! from $
* Changed some commands to be easier to use (in README.md)
* Updated README.md
* added docstring and option to select number of players in secret jarjar

# Version 2.3.0
* Changed command prefix to $ from /
* added help command
* added skeleton of secret jar jar

# Version 2.2.0
* chatbot 2.0!!
* Many improvements have been made to the model that obi wan uses
* trained until loss didn't improve for 5 epochs
* does not need to train every time the bot starts running
    * SIGNIFICANTLY reduces computation strain
* new test function added to Model

# Version 2.1.0
* fixed apostrophe bug (it just disappeared)
* changed /obiwan to /obichat since it's not the only feature of the bot anymore
* removed bug log from repo since there were none anymore

# Version 2.0.1
* fixed README.md

# Version 2.0.0
* Brand new feature!!
* Obi-Wan Kenobot can now say an iconic quote in the voice chat!
* Simply connect to a voice chat and then type /obitalk and Kenobot will join to say a line!
* also minor cahnges to make code more readable
* requirements.txt updated
* README.md updated

# Version 1.0.1
* bot has been deployed on AWS instead of Heroku
* removed Procfile

# Version 1.0.0
* bot has been deployed!!
* Procfile added for deployment
* requirements.txt finalized
* README.md updated

# Version 0.2.1
* bot now responds to user input

# Version 0.2.0
* app is now a discord bot
    * not deployed yet
* model folder is now a package
* data folder is moved to under source folder
* Model is now built by specifying data path
* requirements.txt added
* bot responds with 'hello' when /obiwan command is used

# Version 0.1.0
* model.py is finished and fully functional
  * model can be:
    * printed
    * trained
    * saved
    * loaded

# Version 0.0.3
* model.py can be trained and printed as a string
* Model.py renamed to model.py
* data folder moved to model folder

# Version 0.0.2
* Model.py will create the model and show the summary

# Version 0.0.1
* The class containing the model was created