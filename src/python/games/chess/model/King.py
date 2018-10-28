from Piece import Piece

class King(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "K"

    def __repr__(self):
        return "King"

    def getMoves(self):
        x = 0
        y = 0
        while x < 2:
            while y < 2:
                if self.location[0] + x < 8:
                    if self.location[1] + y < 8:
                        yield (self.location[0] + x, self.location[1] + y)
                    if self.location[1] - y >= 0:
                        yield (self.location[0] + x, self.location[1] - y)
                if self.location[0] - x >= 0:
                    if self.location[1] + y < 8:
                        yield (self.location[0] - x, self.location[1] + y)
                    if self.location[1] - y >= 0:
                        yield (self.location[0] - x, self.location[1] - y)
