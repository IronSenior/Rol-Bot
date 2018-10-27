
from libs import usuario, dados, game, historia
import telebot
import json

bot = telebot.TeleBot("TOKEN")



with open("historia_1.json", "r") as file:
    dct = json.load(file)
    @bot.message_handler(commands=['start', 'help'])
    def start(m):
        cid = m.chat.id
        bot.send_message(cid, dct["0"]["txt"])
