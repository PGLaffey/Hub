from model.Piece import Piece

class King(Piece):
    def __init__(self, location, team, game):
        super().__init__(location, team, game)

    def __str__(self):
        return "K"

    def __repr__(self):
        return "King"

    def getMoves(self):
        for x in range(-1,2):
            for y in range(-1,2):
                newLoc = (self.location[0] + x, self.location[1] + y)
                if self.validMove(newLoc) and newLoc != self.location:
                    yield newLoc




