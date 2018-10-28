from Piece import Piece

class Horse(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "H"

    def __repr__(self):
        return "Horse"

    def getMoves(self):
        newLoc = (self.location[0] + 1, self.location[1] + 2)
        if newLoc[0] < 8 and newLoc[1] < 8:
            yield newLoc
        newLoc = (self.location[0] - 1, self.location[1] + 2)
        if newLoc[0] >= 0 and newLoc[1] < 8:
            yield newLoc            
        newLoc = (self.location[0] - 1, self.location[1] - 2)
        if newLoc[0] >= 0 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (self.location[0] + 1, self.location[1] - 2)
        if newLoc[0] < 8 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (self.location[0] + 2, self.location[1] + 1)
        if newLoc[0] < 8 and newLoc[1] < 8:
            yield newLoc
        newLoc = (self.location[0] + 2, self.location[1] - 1)
        if newLoc[0] < 8 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (self.location[0] - 2, self.location[1] + 1)
        if newLoc[0] >= 0 and newLoc[1] < 8:
            yield newLoc
        newLoc = (self.location[0] - 2, self.location[1] - 1)
        if newLoc[0] >= 0 and newLoc[1] >= 0:
            yield newLoc
