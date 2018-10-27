#Definición de clase historia
import json

class Historia:
    def __init__(self, code):
        self.codigo = code
        self.nombre_arch = "hitoria_" + str(code)
        self.parraf_counter = 0

    def getParrafo(self):
        with open(self.nombre_arch, 'r') as histfile:
            hist = json.load(histfile)
            return hist[self.parraf_counter]

    def setParrafo(self, counter = 0):
        if counter:
            self.parraf_counter = counter
        else:
            self.parraf_counter += 1


