from Piece import Piece

class Bishop(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def getMoves(self):
        for d in range(8):
            if location[0] + d < 8:
                if location[1] + d < 8:
                    yield (location[0] + d, location[1] + d)
                elif location[1] - d >= 0:
                    yield (location[0] + d, location[1] - d)
            elif location[0] - d >= 0:
                if location[1] + d < 8:
                    yield (location[0] - d, location[1] + d)
                elif location[1] - d >= 0:
                    yield (location[0] - d, location[1] - d)
            

