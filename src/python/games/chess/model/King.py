from Piece import Piece

class King(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "K"

    def __repr__(self):
        return "K"

    def getMoves(self):
        x, y = 0
        while x < 2:
            while y < 2:
                if location[0] + x < 8:
                    if location[1] + y < 8:
                        yield (location[0] + x, location[1] + y)
                    if location[1] - y >= 0:
                        yield (location[0] + x, location[1] - y)
                if location[0] - x >= 0:
                    if location[1] + y < 8:
                        yield (location[0] - x, location[1] + y)
                    if location[1] - y >= 0:
                        yield (location[0] - x, location[1] - y)
