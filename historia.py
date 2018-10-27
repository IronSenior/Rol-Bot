#Definición de clase historia
import json

class Historia:

    nombre_arch = ""
    codigo = ""
    parraf_counter = 0

    def __init__(self, code):
        self.codigo = code
        self.nombre_arch = "hitoria_" + str(code)

    def getParrafo():
        with open(self.nombre_arch, 'r') as histfile:
            hist = json.load(histfile)
             return hist[self.parraf_counter]

    def setParrafo(counter = (self.parraf_counter + 1)):
        self.parraf_counter = counter