import telebot
import requests
import random
from flask import Flask,request
from flask_restful import Api,Resource
from dotenv import load_dotenv
import os

load_dotenv()
url="https://pixabay.com/api/?key="+os.getenv("PIC_TOKEN")+"&q={}"
#app=telebot.TeleBot("TOKEN")
#@app.message_handler(commands=['start'])
#def greet(message):
#    app.reply_to(message,f"{message.text}")

#@app.message_handler(func=lambda m:True)
#def photo(message):
#    global url
#    photos=url.format(message.text)
#    req=requests.get(photos).json()
#    #print(req)
#    fn=len(req["hits"])
#    print(random.randrange(0,fn-1,1))
#    app.send_photo(message.chat.id,req["hits"][random.randrange(0,fn-1,1)]["previewURL"])
    #except:
    #    app.reply_to(message,"wrong input")

#app.polling()

bot=Flask(__name__)
api=Api(bot)
class Bot(Resource):
    global url
    def post(self):
        app=telebot.TeleBot(os.getenv("TOKEN"))
        @app.message_handler(func=lambda m:True)
        def photo(message):
            global url
            photos=url.format(message.text)
            req=requests.get(photos).json()

            fn=len(req["hits"])
            print(random.randrange(0,fn-1,1))
            app.send_photo(message.chat.id,req["hits"][random.randrange(0,fn-1,1)]["previewURL"])

        #app.polling()
        return "ok"
    def get(self):
        return "error"

api.add_resource(Bot,'/')
if __name__=='__main__':
    bot.debug=True
    bot.run()
