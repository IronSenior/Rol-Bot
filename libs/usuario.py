import game

class User:
    def __init__(self, uid):
        self._userID = uid
        self._player = game.Player()

    def getID(self):
        return self._userID
        
