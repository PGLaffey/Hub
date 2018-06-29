from python.services.Database import Database
from python.model.User import User
from python.utilities import UtilityMethods
from python.utilities.Printer import *

class Hub():
    def __init__(self):
        self.db = Database()
        self.running = True
        self.initializeCommands()
        self.user = None
        #self.createUser(["DEFAULT", "PASSWORD", 1, 25])
        #self.user = self.attemptLogin("DEFAULT", "PASSWORD")
        self.defaultUser = User("DEFAULT", "PASSWORD", 1, 25)
        self.user = self.defaultUser
        self.getCommand()

    def getCommand(self):
        while self.running:
            printer("Command: ")
            command = input()
            self.processCommand(command)
        printer("Goodbye! :)")
        exit(0)

    def processCommand(self, command):
        command = command.split(" ")
        if command[0].upper() in self.commands:
            self.commands[command.pop(0).upper()](command)
        else:
            printerInvCmd(command)
            

    def createUser(self, attr):
        username = attr[0]
        if self.db.userExists(username):
            printer("User " + username + " already exists.\n")
            return False
        printer("User " + username + " successfully added.\n")
        return self.db.addUser(attr)

    def attemptLogin(self, username, password):
        if password == self.db.getPassword(username):
            printer("Logged into user: " + username + "\n")
            self.user = self.db.getUser(username)
            printerSetUser(self.user)
            return True
        printer("Invalid login credentials.\n")
        return False

##    def printer(self, string):
##        for char in string:
##            print(char, end="")
##            if self.user != None:
##                time.sleep(1/self.user.getSpeed())
##            else:
##                time.sleep(1/25)
##
##    def printerInvCmd(self, arg):
##        self.printer(" ".join(arg) + " is not a valid command. Type 'help' for assistance.\n")
##
##    def printerInvInput(self, response, valid):
##        self.printer("Invalid input: " + response + "\nPlease enter " + valid + ".\n")
                
    def cmdRun(self, arg):
        print("Run command")
        if "".join(arg).upper() == "POKEMONBATTLER":
            print()
            __import__("python.games.pokemon.PokemonBattler")


    def cmdHelp(self, arg):
        print("Help command")

    def cmdQuit(self, arg):
        self.running = False

    def cmdCreate(self, arg):
        if self.user.getPermission() <= 1:
            if arg[0].upper() == "USER":
                return self.cmdCreateUser()
        printerInvCmd(["Create"] + arg)

    def cmdLogin(self, arg):
        login = True
        if self.user != self.defaultUser:
            login = self.cmdLogout(arg)
        if login:
            attributes = ["username", "password"]
            values = []
            count = 0
            while True:
                printer("Enter your " + attributes[count] + ": ")
                ans = input()
                if ans.upper() == "CANCEL":
                    printer("Login cancelled.\n")
                    return False
                elif count == 0:
                    values.append(ans)
                    count += 1
                else:
                    values.append(ans)
                    if self.attemptLogin(values[0], values[1]):
                        return True
                    else:
                        count = 0
        return False

    def cmdLog(self, arg):
        if len(arg) > 0:
            cmd = arg.pop(0)
            if cmd.upper() == "IN":
                return self.cmdLogin(arg)
            elif cmd.upper() == "OUT":
                return self.cmdLogout(arg)
            arg = [cmd] + arg
        printerInvCmd(["Log"] + arg)
        
                

    def cmdLogout(self, arg):
        if self.user != self.defaultUser:
            while True:
                printer("Are you sure you want to log out of user: " + self.user.getUsername() + "\n")
                ans = input()
                if ans.upper() == "YES":
                    self.user = self.defaultUser
                    printer("Logged out of user: " + self.user.getUsername() + "\n") 
                    return True
                elif ans.upper() == "NO" or ans.upper() == "CANCEL":
                    printer("Logout cancelled")
                    return False
                else:
                    printerInvInput(ans, "enter Yes or No")
        printer("Cannot logout, not logged into a user.\n")
            
    def cmdCreateUser(self):
        attributes = ["username", "password", "permission", "speed (Default 25)"]
        values = []
        count = 0
        while count < 4:
            error = None
            printer("Please enter the new users " + attributes[count] + ": ")
            ans = input()
            if ans.upper() == "CANCEL":
                return False
            elif count == 0:
                if self.db.userExists(ans):
                    error = "username already in use"
                else:
                    values.append(ans)
                    count += 1
            elif count == 1:
                values.append(ans)
                count += 1
            elif count == 2:
                if UtilityMethods.isInt(ans):
                    ans = int(ans)
                    if ans >= self.user.getPermission():
                        values.append(ans)
                        count += 1
                    else:
                        ans = "cannot create user with more permissions than yourself"
                        error = "a valid number"
                else:
                    error = "a valid number"
            else:
                if UtilityMethods.isInt(ans):
                    ans = int(ans)
                    values.append(ans)
                    count += 1
                else:
                    error = "a valid number"
            if error != None:
                printerInvInput(ans, error)
        return self.createUser(values)
                
                        

    def initializeCommands(self):
        self.commands = {}
        self.commands["RUN"] = self.cmdRun
        self.commands["QUIT"] = self.cmdQuit
        self.commands["EXIT"] = self.cmdQuit
        self.commands["HELP"] = self.cmdHelp
        self.commands["CREATE"] = self.cmdCreate
        self.commands["LOGIN"] = self.cmdLogin
        self.commands["LOGOUT"] = self.cmdLogout
        self.commands["LOG"] = self.cmdLog
