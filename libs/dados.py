#Clases de dados (d20, d10 y d8)
import random

#Clase que representa un d20
class dado12:
    def __init__(self):
        self.resultado = 0

    def tirada(self):
        self.resultado = random.randint(1,20)
        return self.resultado

#Clase que representa un d10
class dado10:
    def __init__(self):
        self.resultado = 0

    def tirada(self):
        self.resultado = random.randint(1,10)
        return self.resultado

#Clase que representa un d8
class dado8:
    def __init__(self):
        self.resultado = 0

    def tirada(self):
        self.resultado = random.randint(1,8)
        return self.resultado


        
