from abc import ABC, abstractmethod

class Piece(ABC):
 
    def __init__(self, location, team):
        self.location = location
        self.team = team
        super().__init__()
    
    @abstractmethod
    def getMoves(self):
        pass

    def move(self, location):
        self.location = location
