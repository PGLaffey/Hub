from Piece import Piece

class Bishop(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "B"

    def __repr__(self):
        return "Bishop"

    def getMoves(self):
        for d in range(8):
            if self.location[0] + d < 8:
                if self.location[1] + d < 8:
                    yield (self.location[0] + d, self.location[1] + d)
                elif self.location[1] - d >= 0:
                    yield (self.location[0] + d, self.location[1] - d)
            elif self.location[0] - d >= 0:
                if self.location[1] + d < 8:
                    yield (self.location[0] - d, self.location[1] + d)
                elif self.location[1] - d >= 0:
                    yield (self.location[0] - d, self.location[1] - d)
            

