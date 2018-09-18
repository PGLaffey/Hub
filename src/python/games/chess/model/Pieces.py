from Piece import Piece

class Pawn(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self, white, x, y)

    def moves(self):
        if white:
            return [(0,1)]
        return [(0,-1)]

    def attacks(self):
        if white:
            return [(-1,1),(1,1)]
        return [(-1,-1),(1,-1)]

    def toString(self):
        return 'P'


class Rook(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self, white, x, y)

    def moves(self):
        return [(float('-inf'),0),(float('inf'),0),
                (0,float('-inf')),(0,float('inf'))]

    def toString(self):
        return 'R'


class Bishop(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self, white, x, y)

    def moves(self):
        return [(float('inf'),float('inf')),
                (float('inf'),float('-inf')),
                (float('-inf'),float('-inf')),
                (float('-inf'),float('inf'))]

    def toString(self):
        return 'B'               


class Queen(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self,white, x, y)

    def moves(self):
        return [(float('-inf'),float('-inf')),(float('inf'),float('-inf')),
                (float('-inf'),float('-inf')),(float('-inf'),float('inf')),
                (float('-inf'),0),(float('inf'),0),(0,float('-inf')),
                (0,float('inf'))]

    def toString(self):
        return 'Q'


class King(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self, white, x, y)

    def moves(self):
        return [(0,0),(0,1),(1,0),(1,1)]

    def toString(self):
        return 'K'


class Horse(Piece):
    def __init__(self, white, x, y):
        Piece.__init__(self, white, x, y)

    def moves(self):
        return [(0,0),(0,1),(1,0),(1,1)]

    def toString(self):
        return 'H'
