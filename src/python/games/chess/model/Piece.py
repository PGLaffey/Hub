from abc import ABC, abstractmethod

class Piece(ABC):
 
    def __init__(self, location, team):
        self.location = location
        self.team = team
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
