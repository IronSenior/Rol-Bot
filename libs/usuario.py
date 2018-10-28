# -*- coding: utf-8 -*-
import json

#Crea un archivo para el usuario
def create_user(cid):
    file_name = "./DB/users/" + str(cid) + ".json"
    dict = {"ID": str(cid), "parrafo_counter": 0}
    with open(file_name, "w") as jsonfile:
        json.dump(dict, jsonfile, indent=3)

#Devuelve el parrafo por el que va un usuario
def getparrafo(cid):
    file_name = "./DB/users/" + str(cid) + ".json"
    with open(file_name, "r") as jsonfile:
        user_dct = json.load(jsonfile)
        return user_dct["parrafo_counter"]

#Establece el aprrafo por el que va un usuario
def setparrafo(cid, parrafo):
    file_name = "./DB/users/" + str(cid) + ".json"
    with open(file_name, "r") as jsonfile:
        user_dct = json.load(jsonfile)
        user_dct["parrafo_counter"] = parrafo
    with open(file_name, "w") as jsonfile:
        json.dump(user_dct, jsonfile, indent=3)
