from abc import ABC, abstractmethod

class Piece(ABC):
 
    def __init__(self, location, team, game):
        self.location = location
        self.team = team
        self.game = game
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def getMoves(self):
        pass

    def getLocation(self):
        return self.location

    def move(self, location):
        self.location = location

    def validMove(self, newLoc):
        if newLoc[0] < 8 and newLoc[0] >= 0:
            if newLoc[1] < 8 and newLoc[1] >= 0:
                if self.game.noCollision(newLoc, self.team):
                    return True
        return False
