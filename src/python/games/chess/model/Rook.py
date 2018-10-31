from model.Piece import Piece

class Rook(Piece):
    def __init__(self, location, team, game):
        super().__init__(location, team, game)

    def __str__(self):
        return "R"

    def __repr__(self):
        return "Rook"

    def getMoves(self):
        for x in range(8):
            if self.validMove((x, self.location[1])):
                yield (x, self.location[1])
        for y in range(8):
            if self.validMove((self.location[0], y)):
                yield (self.location[0], y)
