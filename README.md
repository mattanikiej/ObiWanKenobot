# Obi-Wan Kenobot
This is a chatbot that mimics Jedi Master Obi-Wan Kenobi from Star Wars episodes 1-3.

![Obi-Wan Kenobi](https://www.tvinsider.com/wp-content/uploads/2021/12/BOBA_FETT_STAR_WARS_5-1014x570.jpg)

## Welcome!
Obi-Wan is the charismatic Jedi Master played by Ewan McGregor in the Star Wars prequel trilogy and features many iconic
lines such as "Oh no. I'm not brave enough for politics" and "Sith Lords are our specialty." This bot aims to decipher 
as best it can the user's intention when speaking to it, and respond with a quote that corresponds to that intent. The 
bot initially started as only a chatbot, but with the release of 2.0 the bot now has other features as well! As of right 
now, the bot is only available on Discord.

## Adding bot to your Discord server
This is the simplest part. Make sure you are an admin on whatever server you want to add it to and click this link
[here](https://discord.com/api/oauth2/authorize?client_id=956584753874743368&permissions=414464609344&scope=bot).

## How it works
The model uses the tensorflow machine learning library to create a text classification model. It then categorizes the
users input and sends out a random response for that category. To use the bot in your Discord server use the command: 
   
__ob!chat \<message\>__  

where __\<message\>__ is replaced with the message you want to send

## Other Features
* __ob!help__
    * Displays all commands and what they do
* __ob!talk__
  * Will join the channel the user is currently in and say a movie quote
* __ob!sjj \<number of players\>__
    * Starts a game of secret jar jar
    * __\<number of players\>__ is replaced with desired amount of players
        * Defaults to 5 which is the minimum
    * NOT FINISHED SO DOES NOTHING RIGHT NOW

## Sources
The data file was created myself using quotes found from the scripts found here: https://imsdb.com/ .   
Audio was taken from Youtube videos. The urls for those can be found in src/bot.py in the obitalk function.

## Authors
Matt Anikiej