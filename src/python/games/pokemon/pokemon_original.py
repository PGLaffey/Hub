class Pokemon(object):
    """Initalizes a Pokemon"""
    def __init__(self, name, element, health, attack, defense):
        """Initalizes the Pokemon with base stats"""
        self.name,self.element,self.health,self.attack,self.defense,self.total_health = name,element.lower(),health,attack,defense,health
        self.type_advantage()

    def type_advantage(self):
        """Sets base type advantages and disadvantages"""
        if self.element == 'fire':
            self.double_defense = ['fire','grass','bug']
            self.half_defense = ['water','ground','rock']
            self.immune = [None]
        elif self.element == 'water':
            self.half_defense = ['electric','grass']
            self.double_defense = ['fire','water','ice']
            self.immune = [None]
        elif self.element == 'electric':
            self.half_defense = ['ground']
            self.double_defense = ['flying','electric']
            self.immune = [None]
        elif self.element == 'grass':
            self.half_defense = ['fire','ice','poison','flying','bug']
            self.double_defense = ['water','electric','grass','ground']
            self.immune = [None]
        elif self.element == 'ice':
            self.half_defense = ['fire','fighting','rock']
            self.double_defense = ['ice']
            self.immune = [None]
        elif self.element == 'fighting':
            self.half_defense = ['flying','psychic']
            self.double_defense = ['bug','rock']
            self.immune = [None]
        elif self.element == 'poison':
            self.half_defense = ['ground','psychic','bug']
            self.double_defense = ['grass','fighting','poison']
            self.immune = [None]
        elif self.element == 'ground':
            self.half_defense = ['water','grass','ice']
            self.double_defense = ['poison','rock']
            self.immune = ['electric']
        elif self.element == 'flying':
            self.half_defense = ['electric','ice','rock']
            self.double_defense = ['grass','fighting','bug']
            self.immune = ['ground']           
        elif self.element == 'psychic':
            self.half_defense = ['bug']
            self.double_defense = ['fighting','pyschic']
            self.immune = ['ghost']
        elif self.element == 'bug':
            self.half_defense = ['fire','poison','flying','rock']
            self.double_defense = ['grass','fighting','ground']
            self.immune = [None]
        elif self.element == 'rock':
            self.half_defense = ['water','grass','fighting','ground']
            self.double_defense = ['normal','fire','poison','flying']
            self.immune = [None]
        elif self.element == 'ghost':
            self.half_defense = ['ghost']
            self.double_defense = ['bug','poison']
            self.immune = ['normal','fighting']           
        elif self.element == 'dragon':
            self.half_defense = ['ice','dragon']
            self.double_defense = ['fire','water','electic','grass']
            self.immune = [None]
        else:
            print('Type error in defense')
        
    def __str__(self):
        """Prints info on Pokemon"""
        return "Pokemon: {}\nType: {}\nHP: {}\nMax HP: {}\nATK: {}\nDEF: {}".format(self.name,self.element,self.health,self.total_health,self.attack,self.defense)

#Change battle.py so that it tests the move type against the defending
#pokemons strengths, weakness' and immunities.

#Add loop to add all pokemon to game and load them into a hash table.
