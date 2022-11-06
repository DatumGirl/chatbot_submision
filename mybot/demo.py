#! /usr/bin/python3
from flask import Flask, render_template, request
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel
from botRespond import getResponse

##Experimental Date Time
from dateTime import getTime, getDate

app = Flask(__name__)

chatbotName = 'Pizzy ChatBot'
botAvatar = '/static/bot.png'

@app.route("/")
def home():
    return render_template("index.html", botName = chatbotName, botAvatar = botAvatar)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    noResponse = ["Call teh customer care "]
    if botReply is "IDKnull":
        botReply = random.choice(noResponse)
    elif botReply is "Enter the reference number to cancel"
        botReply = "Order is cancelled . thank you"
    return botReply

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)
