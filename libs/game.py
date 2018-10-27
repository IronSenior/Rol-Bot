#Definición de clases referentes al juego

class Player:
    def __init__(self, vida=12):
        self._vida = vida
        self._oro = 0

    
class Enemigo:
    def __init__(self):
        #Para la herencia llamamos a la función init de la clase padre
        Player.__init__(self, vida = 6)
        self._loot = 1
    
        
