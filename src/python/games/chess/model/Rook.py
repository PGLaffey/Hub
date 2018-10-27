from Piece import Piece

class Rook(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "R"

    def __repr__(self):
        return "R"

    def getMoves(self):
        for x in range(8):
            yield (x, location[1])
        for y in range(8):
            yield (location[0], y)
