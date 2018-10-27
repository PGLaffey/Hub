from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, game, num):
        self.game = game
        self.num = num

    @abstractmethod
    def takeTurn(self):
        pass
