# Obi-Wan Kenobot
This is a chatbot that mimics Jedi Master Obi-Wan Kenobi from Star Wars episodes 1-3.

![Obi-Wan Kenobi](https://www.tvinsider.com/wp-content/uploads/2021/12/BOBA_FETT_STAR_WARS_5-1014x570.jpg)

## Welcome!
Obi-Wan is the charismatic Jedi Master played by Ewan McGregor in the Star Wars prequel trilogy and features many iconic
lines such as "Oh no. I'm not brave enough for politics" and "Sith Lords are our specialty." This bot aims to decipher 
as best it can the user's intention when speaking to it, and respond with a quote that corresponds to that intent. As of
right now, the bot is only available on Discord.

## Adding bot to your Discord server
This is the simplest part. Make sure you are an admin on whatever server you want to add it to and click this link
[here](https://discord.com/api/oauth2/authorize?client_id=956584753874743368&permissions=414464609344&scope=bot).

## How it works
The model uses the tensorflow machine learning library to create a text classification model. It then categorizes the
users input and sends out a random response for that category. To use the bot in your Discord server use the command: 
   
__/obiwan message__  

where message is the message you want to send

## Authors
Matt Anikiej