from Piece import Piece

class Pawn(Piece):

    def __init__(self, location, team, direct, moved=False):
        """Location - current location of piece
           Direct - U, D, L, R"""
        self.moved = moved
        self.direct = direct
        super().__init__(location, team)

    def getMoves(self):
        distance = 1
        if self.moved == False:
            distance = 2
        if self.direct == 'U':
            #Test generator
            yield ((location[0], y) if x % 2 else x* 100 for d in range(distance))
        elif self.direct == 'D':
            yield ((location[0], location[1] - d - 1) for y in range(distance))
        elif self.direct == 'L':
            yield ((location[0], location[1] - d - 1) for x in range(distance))
            

    def move(self, location):
        self.moved = True
        super().move(location)
