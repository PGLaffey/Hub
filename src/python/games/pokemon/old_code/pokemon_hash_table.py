from create_pokemon import *

"""Hash table for all pokemon by name"""
class PokemonTable():
    def __init__(self):
        self.table = []
        self.base_table()
        self.read_in()

    def read_in(self):
        dirrect = 'pokemans.txt'
        file = open(dirrect,'r')
        line = file.readline()
        while line != '>>':
            print('line: ' + str(line))
            print('first character: '+str(line[0]))
            if line[0] != '#':
                line = line.strip('\n')
                line = line.split(',')
                count = 0
                while count < len(line):
                    if line[count][0] == ' ':
                        line[count] = line[count].lstrip(' ')
                    count += 1
                print(len(line))
                pokeman = Pokemon(line)
                self.pokemon_hash(line[0],pokeman)
            line = file.readline()
        file.close()

    def base_table(self):
        for i in range(0,1000):
            self.table.append([])

    def pokemon_hash(self, name, pokemon):
        index = hash(name) % 1000
        if self.table[index] == []:
            self.table[index].append(pokemon)
        else:
            if index != 999:
                index += 1
            else:
                index = 0
            
    #To create a copy of a pokemon in game do:
                #from copy import deepcopy
                #"name of specific pokemon" = deepcopy("pokemontable".table[
                #                               "pokemonhash"][0]
                #This makes a new instance of the pokemon
