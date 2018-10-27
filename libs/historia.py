#Definición de clase historia
import json

def getHistoria():
    with open("historia_1.json", "r") as file:
        dct = json.load(file)
        return dct


def getKayboard(dct = getHistoria(), parrafo):
        #Nombre del teclado, se llama a él desde bot.py
        keyboard_historia = types.InlineKeyboardMarkup()
        parrafo = str(parrafo)
        if dct[parrafo]["numero_opciones"] == 2:
            #Añade los botones con su texto, y el valor que devuelve cada botón cuando es clickado
            keyboard_historia.add(types.InlineKeyboardButton(dct[parrafo]["op_1"]["texto"], callback_data = "op_1"),
                             types.InlineKeyboardButton(dct[parrafo]["op_2"]["texto"], callback_data = "op_2"),
            )
        else:
            #Añade los botones con su texto, y el valor que devuelve cada botón cuando es clickado
            keyboard_historia.add(types.InlineKeyboardButton(dct[parrafo]["op_1"]["texto"], callback_data = "op_1"),
                             types.InlineKeyboardButton(dct[parrafo]["op_2"]["texto"], callback_data = "op_2"),
                             types.InlineKeyboardButton(dct[parrafo]["op_3"]["texto"], callback_data = "op_3"),
            )

        return dct[parrafo]["txt"], keyboard_historia

def getsigparrafo(ant_parrafo, op):
    dct = getHistoria()
    return dct[op]["puntero"]
