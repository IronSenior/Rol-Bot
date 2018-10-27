# -*- coding: utf-8 -*-
#Definicion de clase historia
import json
from telebot import *

def getHistoria():
    with open("./libs/historia_1.json", "r") as file:
        dct = json.load(file)
        return dct


def getKayboard(parrafo, dct = getHistoria()):
        #Nombre del teclado, se llama a el desde bot.py
        keyboard_historia = types.InlineKeyboardMarkup()
        parrafo = str(parrafo)
        if dct[parrafo]["numero_opciones"] == 2:
            #Anade los botones con su texto, y el valor que devuelve cada boton cuando es clickado
            keyboard_historia.add(types.InlineKeyboardButton(dct[parrafo]["op_1"]["texto"], callback_data = "op_1"),
                             types.InlineKeyboardButton(dct[parrafo]["op_2"]["texto"], callback_data = "op_2"),
            )
        else:
            #Anade los botones con su texto, y el valor que devuelve cada boton cuando es clickado
            keyboard_historia.add(types.InlineKeyboardButton(dct[parrafo]["op_1"]["texto"], callback_data = "op_1"),
                             types.InlineKeyboardButton(dct[parrafo]["op_2"]["texto"], callback_data = "op_2"),
                             types.InlineKeyboardButton(dct[parrafo]["op_3"]["texto"], callback_data = "op_3"),
            )

        return dct[parrafo]["txt"], keyboard_historia

def getsigparrafo(ant_parrafo, op):
    dct = getHistoria()
    return dct[str(ant_parrafo)][str(op)]["puntero"]
