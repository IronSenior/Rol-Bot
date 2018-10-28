# -*- coding: utf-8 -*-
from libs import usuario, historia
import telebot
import json

bot = telebot.TeleBot("")

#Empieza la historia y crea el archivo de usuario
@bot.message_handler(commands=['start', 'help'])
def start(m):
    cid = m.chat.id
    usuario.create_user(cid)
    message, keyb = historia.getKayboard(parrafo=0)
    bot.send_message(cid, message, reply_markup = keyb)


#Recoge la opcion escogida por el usuario u manda el siguiente parrafo
@bot.callback_query_handler(func = lambda op: op.data in ["op_1", "op_2", "op_3"])
def parrafo_siguiente(op):
    
    cid = op.message.chat.id
    ant_parrafo = usuario.getparrafo(cid)
    #Un try para recoger todos los errores por estar en desarrollo
    try:
        sig_parrafo = historia.getsigparrafo(ant_parrafo, op.data)
        usuario.setparrafo(cid, sig_parrafo)

        message, keyb = historia.getKayboard(parrafo= sig_parrafo)
        bot.send_message(cid, message, reply_markup = keyb)
    except:
        bot.send_message(cid, "Has muerto por tonto (En desarrollo)")


#Seria preferible hacerlo sin polling
bot.polling(none_stop=True, timeout=100)