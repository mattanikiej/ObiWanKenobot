# Obi-Wan Kenobot
This is a chatbot that mimics Jedi Master Obi-Wan Kenobi from Star Wars episodes 1-3.

![Obi-Wan Kenobi](https://www.tvinsider.com/wp-content/uploads/2021/12/BOBA_FETT_STAR_WARS_5-1014x570.jpg)

## Welcome!
Obi-Wan is the charismatic Jedi Master played by Ewan McGregor in the Star Wars prequel trilogy and features many iconic
lines such as "Oh no. I'm not brave enough for politics" and "Sith Lords are our specialty." This bot aims to decipher 
as best it can the user's intention when speaking to it, and respond with a quote that corresponds to that intent.

## How it works
Currently, the model is made using tensorflow and the data is created by myself and the quotes were taken found from 
scripts taken from here: https://imsdb.com/. The model features an embedding layer to make each word a fixed length, 
and LSTM layer to discover sequences and patterns in the inputs.

## Authors
Matt Anikiej