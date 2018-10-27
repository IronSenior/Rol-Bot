# -*- coding: utf-8 -*-
from libs import usuario, historia
import telebot
import json

bot = telebot.TeleBot("599981179:AAEdRsgEV5KJFvK-A7GJlMU90vgI2qHa0Gk")


@bot.message_handler(commands=['start', 'help'])
def start(m):
    cid = m.chat.id
    usuario.create_user(cid)
    message, keyb = historia.getKayboard(parrafo=0)
    bot.send_message(cid, message, reply_markup = keyb)


@bot.callback_query_handler(func = lambda op: op.data in ["op_1", "op_2", "op_3"])
def parrafo_siguiente(op):
    cid = op.message.chat.id
    ant_parrafo = usuario.getparrafo(cid)

    sig_parrafo = historia.getsigparrafo(ant_parrafo, op.data)
    usuario.setparrafo(cid, sig_parrafo)

    message, keyb = historia.getKayboard(parrafo= sig_parrafo)
    bot.send_message(cid, message, reply_markup = keyb)


bot.polling(none_stop=True, timeout=100)