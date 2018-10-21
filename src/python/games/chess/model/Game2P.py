from Bishop import Bishop
from King import King
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from Horse import Horse
import sys

class Game2P():
    def __init__(self, team1=[], team2=[]):
        self.team1 = team1
        self.team2 = team2
        if self.isNewGame():
            self.initializePlayers()

    def isNewGame(self):
        if self.team1 or self.team2:
            return False
        return True

    def initializePlayers(self):
        print("Initializing New Game", sys.err)
        self.team1 = self.initializePlayer('U', 1)
        self.team2 = self.initializePlayer('D', 2)

    def initializePlayer(self, direct, team):
        pieces = []
        y1 = 0
        y2 = 1
        if direct == 'D':
            y1 = 7
            y2 = 6
        for d in range(8):
            pieces.append(Pawn((d,y1), team, direct))
            if d == 0 or d == 7:
                pieces.append(Rook((d,y2), team))
            elif d == 1 or d == 6:
                pieces.append(Horse((d,y2), team))
            elif d == 2 or d == 5:
                pieces.append(Bishop((d,y2), team))
            elif d == 3:
                if team == 1:
                    pieces.append(King((d,y2), team))
                else:
                    pieces.append(Queen((d,y2), team))
            else:
                if team == 1:
                    pieces.append(Queen((d,y2), team))
                else:
                    pieces.append(King((d,y2), team))
        return pieces

            
