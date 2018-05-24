"""Bulbasaur vs Charmander"""
from pokemon_original import *
from typer import *
from escape import *
from battle import *
from move import *

rawmoves = Move_Table()
moves = rawmoves.table

pokemon1 = Pokemon('Charmander','fire',200,10,5)
wild_pokemon = Pokemon('Bulbasaur','grass',150,7,12)
o = Pokemon("Onix",'earth',300,5,20)

typer('A wild Bulbasaur has appeared!\n')

a =Battle(pokemon1,wild_pokemon)
wild_pokemon.health = 150
b = Battle(o,wild_pokemon)
pokemon1.health = 200
o.health = 300
c= Battle(pokemon1,o)

typer('Game Over')
