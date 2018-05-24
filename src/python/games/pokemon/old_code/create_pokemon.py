from move import *

class Pokemon(object):
    """Initalizes a Pokemon"""
    def __init__(self, attributes):
        """Initalizes the Pokemon with base stats"""
        self.name,self.element1,self.element2,self.hp,self.attack,self.defense,self.speed = attributes[0],attributes[1],attributes[2],int(attributes[3]),int(attributes[4]),int(attributes[5]),int(attributes[6])
        self.maxhp = self.hp
        self.level = 1
        self.moves = [None,None,None,None]
        
    def __str__(self):
        """Prints info on Pokemon"""
        return "Pokemon: {}\nType: {}\nLVL: {}\nHP: {}\nMax HP: {}\nATK: {}\nDEF: {}\nSPE: {}".format(self.name,(self.element1,self.element2),self.level,self.hp,self.maxhp,self.attack,self.defense,self.speed)

    def level_up(self):
        """Levels up pokemons stats 1 level"""
        self.level += 1
        self.hp,self.maxhp,self.attack,self.defense,self.speed = self.hp*1.03,self.maxhp*1.03,self.attack*1.03,self.defense*1.03,self.speed*1.03
        
    def set_move(self,move,slot):
        """Sets 1st move. Takes move as (name,type)"""
        all_moves = Move_Table()
        move_index = hash(move[0])%26
        count = 0
        finished = False
        while not finished:
            try:
                if move[0] in all_moves.table[move[1]][move_index][count]:
                    finished = True
                    self.moves[slot] = all_moves.table[move[1]][move_index][count]
                    print('Move: '+move+', Set to slot: '+slot)
                else:
                    count += 1
            except IndexError:
                finished = True
                print('Error, Move "'+move+'" Not Found')
