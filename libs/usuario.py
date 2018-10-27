#Clase usuario (Quizas solo se quede en json)
import game

class User:
    def __init__(self, uid):
        self._userID = uid
        self._player = game.Player()

    #Devuelve la id
    def getID(self):
        return self._userID
        
