from Piece import Piece

class Pawn(Piece):

    def __init__(self, location, team, direct, game, moved=False):
        """Location - current location of piece
           Direct - U, D, L, R"""
        self.moved = moved
        self.game = game
        self.direct = direct
        super().__init__(location, team)

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
            if self.moved == False:
                distance = 2
            while distance > 0:
                if self.direct == 'U' and self.location[1] < 7:
                    newLoc = (self.location[0], self.location[1] + distance)
                elif self.direct == 'D' and self.location[1] > 0:
                    newLoc = (self.location[0], self.location[1] - distance)
                elif self.direct == 'L' and self.location[0] > 0:
                    newLoc = (self.location[0] - distance, self.location[1])
                elif self.direct == 'R' and self.location[0] < 7:
                    newLoc = (self.location[0] + distance, self.location[1])
                if self.game.noCollision(newLoc, self.team):
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
