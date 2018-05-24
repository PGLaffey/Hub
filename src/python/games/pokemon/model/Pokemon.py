

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
           self.statsUp()

    def statsUp(self):
        pass

    def levelUp(self):
        self.statsUp()
        if self.level == self.evoLevel:
            self.evolve()

    def __str__(self):
        return """Pokemon: {}\n
                  Level:   {}\n
                  Type:    {} {}\n
                  HP:      {}/{}\n
                  ATK:     {}\n
                  DEF:     {}\n
                  SAK:     {}\n
                  SDF:     {}\n
                  SPD:     {}\n""".format(self.name,self.level,self.element1,self.element2,self.health,self.maxHealth,self.attack,self.defense,self.specialAttack,self.specialDefence,self.speed)
