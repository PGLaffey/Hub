from python.games.pokemon.model.Pokemon import Pokemon
from python.games.pokemon.service.Database import Database
from python.utilities.Printer import *
from python.utilities.UtilityMethods import *
from python.utilities.Globals import POKEMONTYPES

class PokemonBattler():
    def __init__(self):
        self.database = Database()
        self.running = True
        self.initializeCommands()
        self.start()

    def start(self):
        printer(("Welcome to Pokemon Battler!\n"
                 "Here you can emulate any Pokemon battle.\n"))
        self.getCommand()

    def printPokemonList(self, gen, elements):
        printer("ID | Name\n")
        pokemon = self.database.getNames(gen, elements)
        pmList = sorted(pokemon)
        for pmID in pmList:
            name = pokemon[pmID]
            pmID = ('0' * (3 - len(str(pmID)))) + str(pmID)
            printer(pmID + "|" + name + "\n")

    def getArgElements(self, arg):
        elements = []
        while len(arg) > 0:
            element = arg.pop(0).upper()
            if element in POKEMONTYPES:
                elements.append(element)
            else:
                printer(element + " is not a valid type.\n")
        return elements

    def cmdShowPokemon(self, arg):
        if len(arg) > 0:
            cmd = arg.pop(0)
            if cmd.upper() == "ALL":
                elements = self.getArgElements(arg)
                return self.printPokemonList(0, elements)
            elif isInt(cmd):
                elements = self.getArgElements(arg)
                return self.printPokemonList(int(cmd), elements)
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

    def cmdCreate(self, arg):
        print("Create command")

    def cmdQuit(self, arg):
        self.running = False

    def cmdHelp(self, arg):
        print("Help command")

    def getCommand(self):
        while self.running:
            printer("Command: ")
            command = input()
            self.processCommand(command)
        printer("Returning to main application.\n\n")

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
