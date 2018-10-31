from model.Piece import Piece

class Horse(Piece):
    def __init__(self, location, team, game):
        super().__init__(location, team, game)

    def __str__(self):
        return "H"

    def __repr__(self):
        return "Horse"

    def getMoves(self):
        newLoc = (self.location[0] + 1, self.location[1] + 2)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] - 1, self.location[1] + 2)
        if self.validMove(newLoc):
            yield newLoc            
        newLoc = (self.location[0] - 1, self.location[1] - 2)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] + 1, self.location[1] - 2)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] + 2, self.location[1] + 1)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] + 2, self.location[1] - 1)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] - 2, self.location[1] + 1)
        if self.validMove(newLoc):
            yield newLoc
        newLoc = (self.location[0] - 2, self.location[1] - 1)
        if self.validMove(newLoc):
            yield newLoc
