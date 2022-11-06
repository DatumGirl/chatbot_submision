#! /usr/bin/python3
from flask import Flask, render_template, request
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel
from botRespond import getResponseOrder, getResponseCancel,getResponse
import random

##Experimental Date Time
from dateTime import getTime, getDate

application = Flask(__name__)

chatbotName = "Pizzy"

#myBotName
print("Bot Name set to: " + chatbotName)
print("Background is " + chatBG)
print("Avatar is " + botAvatar)
print("Confidence level set to " + str(confidenceLevel))

#Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

def tryGoogle(myQuery):
	#print("<br>Try this from my friend Google: <a target='_blank' href='" + j + "'>" + query + "</a>")
	return "<br><br>You can try this from my friend Google: <a target='_blank' href='https://www.google.com/search?q=" + myQuery + "'>" + myQuery + "</a>"

@application.route("/")
def home():
    return render_template("index.html", botName = chatbotName, chatBG = chatBG, botAvatar = botAvatar)

@application.route("/get")
def get_bot_response_Order():
    
    userText = request.args.get('msg')
    botReply = str(getResponseOrder(userText))
    ref =str(random.randint(10000,50000))
    if botReply == "IDKresponse":
        botReply = str(getResponseOrder('IDKnull')) ##Send the i don't know code back to the DB
        if useGoogle == "yes":
            botReply = "please call customer care"
    elif botReply == "Order confirmed" :
        botReply = botReply + ".Here is the reference number : "+ref
               
    return botReply
 

if __name__ == "__main__":
   
    application.run()
      
