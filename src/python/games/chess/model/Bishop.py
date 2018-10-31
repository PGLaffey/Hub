from model.Piece import Piece

class Bishop(Piece):
    def __init__(self, location, team, game):
        super().__init__(location, team, game)

    def __str__(self):
        return "B"

    def __repr__(self):
        return "Bishop"
            
    def getMoves(self):
        for d in range(-8,8):
            newLoc = (self.location[0] + d, self.location[1] + d)
            if self.validMove(newLoc) and newLoc != self.location:
                yield newLoc
            newLoc = (self.location[0] - d, self.location[1] + d)
            if self.validMove(newLoc) and newLoc != self.location:
                yield newLoc
            
            
                
