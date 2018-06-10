from python.games.pokemon.model.Pokemon import Pokemon
from python.games.pokemon.service.Database import Database
from python.utilities.Printer import *

class PokemonBattler():
    def __init__(self):
        self.database = Database()
        self.pokemonNames = self.database.getAllNames(1)
        self.start()

    def start(self):
        printer(("Welcome to Pokemon Battler!\n"
                 "Here you can emulate any Pokemon battle.\n"))

PokemonBattler()
