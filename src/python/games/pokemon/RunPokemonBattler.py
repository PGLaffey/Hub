from model.Pokemon import Pokemon
from service.Database import Database

class RunPokemonBattler():
    def __init__(self):
        self.database = Database()
        self.pokemonNames = self.database.getAllNames(1)
        print("All Pokemon: ")
        for name, pmID in self.pokemonNames.items():
            print("ID: " + str(pmID) + " Name: " + name)

RunPokemonBattler()
