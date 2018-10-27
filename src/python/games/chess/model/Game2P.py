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

    def __repr__(self):
        return """Team 1: \n
                  {}\n\n
                  Team 2: \n
                  {}""".format(self.team1, self.team2)

    def __str__(self):
        board = ""
        for i in range(8):
            for j in range(8):
                board += "+-"
            board += "+\n"
            for k in range(8):
                board += "| "
            board += "|\n"
        for j in range(8):
            board += "+-"
        board += "+\n"
        for team in (self.team1, self.team2):
            for piece in team:
                loc = piece.getLocation()
                strLoc = 19 + loc[1] * 36 + (loc[0] * 2)
                board = board[:strLoc] + piece.__str__() + board[strLoc + 1:]
        return board

    def printBoard(self):
        pieces1 = [[' ' for i in range(8)] for k in range(8)]
        for piece in self.team1:
            loc = piece.getLocation()
            pieces1[loc[1]][loc[0]] = piece.__str__()
        pieces2 = [[' ' for i in range(8)] for k in range(8)]
        for piece in self.team2:
            loc = piece.getLocation()
            pieces2[loc[1]][loc[0]] = piece.__str__()
        for i in range(8):
            self.printSeperator()
            for k in range(8):
                print("|", end='')
                if pieces1[i][k] != ' ':
                    print(pieces1[i][k], file=sys.stderr, end='')
                elif pieces2[i][k] != ' ':
                    print(pieces2[i][k], end='')
                else:
                    print(" ", end='')
            print("|")
        self.printSeperator()
        
    def printSeperator(self):
        print(("+-" * 8) + "+")

    def isNewGame(self):
        if self.team1 or self.team2:
            return False
        return True

    def initializePlayers(self):
        print("Initializing New Game", file=sys.stderr)
        self.team1 = self.initializePlayer('U', 1)
        self.team2 = self.initializePlayer('D', 2)

    def initializePlayer(self, direct, team):
        pieces = []
        y1 = 1
        y2 = 0
        if direct == 'U':
            y1 = 6
            y2 = 7
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

    def checkAttack(self, piece):
        if piece.team == 1:
            piece = self.findPiece(piece.getLocation(), self.team2)
            if piece:
                self.team2.remove(piece)
        elif piece.team == 2:
            piece = self.findPiece(piece.getLocation(), self.team1)
            if piece:
                self.team1.remove(piece)

    def findPiece(self, loc, team):
        for piece in team:
            if piece.getLocation() == loc:
                return piece
        return False

    def getPieces(self, playerNum):
        if playerNum == 1:
            return self.team1
        elif playerNum == 2:
            return self.team2
        return False