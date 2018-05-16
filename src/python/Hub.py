import time
from python.services.Database import Database
from python.model.User import User

class Hub():
    def __init__(self):
        self.db = Database()
        self.running = True
        self.initializeCommands()
        self.user = None
        self.createUser("DEFAULT", "PASSWORD")
        self.user = self.attemptLogin("DEFAULT", "PASSWORD")
        self.getCommand()

    def getCommand(self):
        while self.running:
            self.printer("Command: ")
            command = input()
            self.processCommand(command)
        self.printer("Goodbye! :)")
        exit(0)

    def processCommand(self, command):
        command = command.split(" ")
        if command[0].upper() in self.commands:
            self.commands[command.pop(0).upper()](command)
        else:
            self.printer(" ".join(command) + " is not a valid command. Type 'help' for assistance\n")
            

    def createUser(self, username, password, permission = 1, speed = 25):
        if not self.db.userExists(username):
            attr = [username, password, permission, speed]
            self.db.addUser(attr)
            self.printer("User " + username + " successfully added.\n")
        else:
            self.printer("User " + username + " already exists.\n")

    def login(self):
        print("login")

    def attemptLogin(self, username, password):
        if password == self.db.getPassword(username):
            self.printer("Logged into user: " + username + "\n")
            return self.db.getUser(username)
        self.printer("Invalid login credentials.\n")
        return None

    def printer(self, string):
        for char in string:
            print(char, end="")
            if self.user != None:
                time.sleep(1/self.user.getSpeed())
            else:
                time.sleep(1/25)
                
    def cmdRun(self, arg):
        print("Run command")

    def cmdHelp(self, arg):
        print("Help command")

    def cmdQuit(self, arg):
        self.running = False


    def initializeCommands(self):
        self.commands = {}
        self.commands["RUN"] = self.cmdRun
        self.commands["QUIT"] = self.cmdQuit
        self.commands["EXIT"] = self.cmdQuit
        self.commands["HELP"] = self.cmdHelp
