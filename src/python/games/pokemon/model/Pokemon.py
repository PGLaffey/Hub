from python.games.pokemon.service.Database import Database

class Pokemon(object):
    def __init__(self, db, pmID, level = 1, moves = None, name = None, owner = None):
        self.initialize(db, pmID)
        self.setLevel(level)
        if moves != None:
            self.moves = moves
        if name != None:
            self.name = name
        if owner != None:
            self.owner = owner

    def initialize(self, db, pmID):
        attr = db.loadPokemonAttr(pmID)
        self.pmID = attr[0]
        self.name = attr[1]
        self.element1 = attr[2]
        self.element2 = attr[3]
        self.total = attr[4]
        self.health = attr[5]
        self.maxHealth = attr[5]
        self.attack = attr[6]
        self.defense = attr[7]
        self.specialAttack = attr[8]
        self.specialDefense = attr[9]
        self.speed = attr[10]
        self.generation = attr[11]

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
