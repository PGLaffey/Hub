from Piece import Piece

class Horse(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def getMoves(self):
        newLoc = (location[0] + 1, location[1] + 2)
        if newLoc[0] < 8 and newLoc[1] < 8:
            yield newLoc
        newLoc = (location[0] - 1, location[1] + 2)
        if newLoc[0] >= 0 and newLoc[1] < 8:
            yield newLoc            
        newLoc = (location[0] - 1, location[1] - 2)
        if newLoc[0] >= 0 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (location[0] + 1, location[1] - 2)
        if newLoc[0] < 8 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (location[0] + 2, location[1] + 1)
        if newLoc[0] < 8 and newLoc[1] < 8:
            yield newLoc
        newLoc = (location[0] + 2, location[1] - 1)
        if newLoc[0] < 8 and newLoc[1] >= 0:
            yield newLoc
        newLoc = (location[0] - 2, location[1] + 1)
        if newLoc[0] >= 0 and newLoc[1] < 8:
            yield newLoc
        newLoc = (location[0] - 2, location[1] - 1)
        if newLoc[0] >= 0 and newLoc[1] >= 0:
            yield newLoc
