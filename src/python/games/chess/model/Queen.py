from model.Piece import Piece

class Queen(Piece):
    def __init__(self, location, team, game):
        super().__init__(location, team, game)

    def __str__(self):
        return "Q"

    def __repr__(self):
        return "Queen"

    def getMoves(self):
        for x in range(-8,8):
            for y in range(-8,8):
                newLoc = (self.location[0] + x, self.location[1] + y)
                if self.validMove(newLoc) and newLoc != self.location:
                    yield newLoc
