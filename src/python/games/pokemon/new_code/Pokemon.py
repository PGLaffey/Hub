

class Pokemon(object):
    def __init__(self, pmID, level = 1, moves = none, name = none, owner = none):
        self.initialize(pmID)
        self.setLevel(level)
        if moves != none:
            self.moves = moves
        if name != none:
            self.name = name
        if owner != none:
            self.owner = owner

    def initialize(self, pmID):
        pass

    def setLevel(self, level):
        for i in range(1, level):
           self.levelUp()

    def levelUp(self):
        pass