from python.games.pokemon.model.Pokemon import Pokemon
from python.games.pokemon.service.Database import Database
from python.utilities.Printer import *
from python.utilities.UtilityMethods import *

class PokemonBattler():
    def __init__(self):
        self.database = Database()
        self.pokemonNames = self.database.getAllNames(1)
        self.running = True
        self.initializeCommands()
        self.start()

    def start(self):
        printer(("Welcome to Pokemon Battler!\n"
                 "Here you can emulate any Pokemon battle.\n\n"))
        self.getCommand()

    def printPokemonList(self, gen):
        printer("ID | Name\n")
        pokemon = self.database.getAllNames(gen)
        for name, pmID in pokemon.items():
            pmID = ("0" * (len(str(pmID)) - 3)) + str(pmID)
            printer(pmID + "|" + name + "\n")

    def cmdShowPokemon(self, arg):
        if len(arg) > 0:
            cmd = arg.pop(0)
            if cmd.upper() == "ALL":
                printPokemonList(0)
            elif isInt(cmd):
                printPokemonList(int(cmd))
            arg = [cmd] + arg
        printerInvCmd(["Show", "Pokemon"] + arg)

    def cmdShow(self, arg):
        if len(arg) > 0:
            cmd = arg.pop(0)
            if cmd.upper() == "POKEMON":
                return self.cmdShowPokemon(arg)
            elif cmd.upper() == "MOVES":
                return self.cmdShowMoves(arg)
            arg = [cmd] + arg
        printerInvCmd(["Show"] + arg)

    def cmdQuit(self, arg):
        self.running = False

    def getCommand(self):
        while self.running:
            printer("Command: ")
            command = input()
            self.processCommand(command)
        printer("Goodbye! :)")

    def processCommand(self, command):
        command = command.split(" ")
        if command[0].upper() in self.commands:
            self.commands[command.pop(0).upper()](command)
        else:
            printerInvCmd(command)

    def initializeCommands(self):
        self.commands = {}
        self.commands["SHOW"] = self.cmdShow
        self.commands["QUIT"] = self.cmdQuit
        self.commands["EXIT"] = self.cmdQuit
        self.commands["HELP"] = self.cmdHelp
        self.commands["CREATE"] = self.cmdCreate

PokemonBattler()
