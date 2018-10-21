from Pieces import *
import sys

ROWS = ['A','B','C','D','E','F','G','H']

class Board():
    def __init__(self):
        self.board = []
        for y in range(8):
            self.board.append([])
            for x in range(8):
                piece = None
                if y < 1:
                    piece = self.initializePiece(x, False)
                elif y < 2:
                    piece = Pawn(False, x, y)
                elif y > 6:
                    piece = self.initializePiece(x, True)
                elif y > 5:
                    piece = Pawn(True, x, y)
                self.board[y].append(piece)

    def get(self, coords):
        y = ROWS.index(coords[0])
        x = coords[1]
        return self.board[y][x]

    def initializePiece(self, x, white):
        y = 0
        if white:
            y = 8
        if x < 1 or x > 6:
            return Rook(white, x, y)
        elif x < 2 or x > 5:
            return Horse(white, x, y)
        elif x < 3 or x > 4:
            return Bishop(white, x, y)
        elif x == 3:
            if white:
                return Queen(white, x, y)
            return King(white, x, y)
        if white:
            return King(white, x, y)
        return Queen(white, x, y)

    def toString(self):
        print("   1 2 3 4 5 6 7 8 ")
        for y in range(8):
            row = self.board[y]
            print("  +-+-+-+-+-+-+-+-+")
            print(ROWS[y], end=" ")
            for cell in row:
                print("|", end="")
                if cell == None:
                    print(" ", end="")
                elif cell.white:
                    print(cell.toString(), end="", file=sys.stderr)
                else:
                    print(cell.toString(), end="")
            print("|")
        print("  +-+-+-+-+-+-+-+-+")
