from model.Piece import Piece

class Pawn(Piece):

    def __init__(self, location, team, game, direct, moved=False):
        """Location - current location of piece
           Direct - U, D, L, R"""
        self.moved = moved
        self.direct = direct
        super().__init__(location, team, game)

    def __str__(self):
        return "P"

    def __repr__(self):
        return "Pawn"

    def getMoves(self):
        attacks = list(self.game.getPawnAttacks(self.location, self.team))
        if attacks:
            for attack in attacks:
                yield attack
        else:
            distance = 1
            if not self.moved:
                distance = 2
            while distance > 0:
                if self.direct == 'U':
                    newLoc = (self.location[0], self.location[1] - distance)
                elif self.direct == 'D':
                    newLoc = (self.location[0], self.location[1] + distance)
                elif self.direct == 'L':
                    newLoc = (self.location[0] - distance, self.location[1])
                elif self.direct == 'R':
                    newLoc = (self.location[0] + distance, self.location[1])
                if self.validMove(newLoc):
                    yield newLoc
                distance -= 1
        self.checkUpgrade()
        
    def checkUpgrade(self):
        if self.direct == 'U' and self.location[1] == 7:
            self.game.doPawnUpgrade(self.location, self.team)
        elif self.direct == 'D' and self.location[1] == 0:
            self.game.doPawnUpgrade(self.location, self.team)
        elif self.direct == 'L' and self.location[0] == 0:
            self.game.doPawnUpgrade(self.location, self.team)
        elif self.direct == 'R' and self.location[0] == 7:
            self.game.doPawnUpgrade(self.location, self.team)

    def move(self, location):
        self.moved = True
        super().move(location)
