class Piece():
    def __init__(self, white, x, y):
        self.white = white
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def moves(self):
        return []

    def attacks(self):
        return moves

    
