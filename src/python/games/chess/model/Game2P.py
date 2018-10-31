from model.Bishop import Bishop
from model.King import King
from model.Pawn import Pawn
from model.Queen import Queen
from model.Rook import Rook
from model.Horse import Horse
import sys

class Game2P():
    def __init__(self, team1=[], team2=[]):
        self.team1 = team1
        self.team2 = team2
        self.converter = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H"}
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
        print("  A B C D E F G H")
        for i in range(8):
            self.printSeperator()
            print(str(i + 1), end='')
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
        print(" " + ("+-" * 8) + "+")

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
            pieces.append(Pawn((d,y1), team, self, direct))
            if d == 0 or d == 7:
                pieces.append(Rook((d,y2), team, self))
            elif d == 1 or d == 6:
                pieces.append(Horse((d,y2), team, self))
            elif d == 2 or d == 5:
                pieces.append(Bishop((d,y2), team, self))
            elif d == 3:
                if team == 1:
                    pieces.append(King((d,y2), team, self))
                else:
                    pieces.append(Queen((d,y2), team, self))
            else:
                if team == 1:
                    pieces.append(Queen((d,y2), team, self))
                else:
                    pieces.append(King((d,y2), team, self))
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

    def getPawnAttacks(self, loc, team):
        if team == 1:
            newLoc = (loc[0] + 1, loc[1] - 1)
            if self.findPiece(newLoc, self.team2):
                yield newLoc
            newLoc = (loc[0] - 1, loc[1] - 1)
            if self.findPiece(newLoc, self.team2):
                yield newLoc
        else:
            newLoc = (loc[0] + 1, loc[1] + 1)
            if self.findPiece(newLoc, self.team1):
                yield newLoc
            newLoc = (loc[0] - 1, loc[1] + 1)
            if self.findPiece(newLoc, self.team1):
                yield newLoc

    def noCollision(self, loc, team):
        if team == 1:
            if self.findPiece(loc, self.team2):
                return True
        else:
            if self.findPiece(loc, self.team1):
                return True
        return False

    def doPawnUpgrade(self, loc, team):
        valid = {"queen": Queen,
                 "rook": Rook,
                 "bishop": Bishop,
                 "horse": Horse}
        self.printBoard()
        print("One of your Pawns have reached your opponents end. You must now promote it.")
        while True:
            ans = input("What would you like to promote it to? ")
            if ans.lower() in valid.keys():
                piece = valid.get(ans.lower())(loc, team)
                if team == 1:
                    self.team1.remove(self.findPiece(loc, self.team1))
                    self.team1.append(piece)
                else:
                    self.team2.remove(self.findPiece(loc, self.team2))
                    self.team2.append(piece)
                break
            print(ans + " is not a valid response. Please enter Queen, Rook, Bishop or Horse.")
            
    def isGameOver(self):
        kings = 0
        for piece in self.team1:
            if type(piece) is King:
                kings += 1
        for piece in self.team2:
            if type(piece) is King:
                kings += 1
        return kings < 2
