import time
from python.services.Database import Database
from python.model.User import User
from python.utilities import Utilities

class Hub():
    def __init__(self):
        self.db = Database()
        self.running = True
        self.initializeCommands()
        self.user = None
        self.createUser(["DEFAULT", "PASSWORD", 1, 25])
        self.defaultUser = User("DEFAULT", "PASSWORD", 1, 25)
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
            self.printerInvCmd(command)
            

    def createUser(self, attr):
        username = attr[0]
        if not self.db.userExists(username):
            self.db.addUser(attr)
            self.printer("User " + username + " successfully added.\n")
        else:
            self.printer("User " + username + " already exists.\n")

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

    def printerInvCmd(self, arg):
        self.printer(" ".join(arg) + " is not a valid command. Type 'help' for assistance.\n")

    def printerInvIn(self, response, valid):
        self.printer("Invalid input: " + response + "\nPlease enter " + valid + ".\n")
                
    def cmdRun(self, arg):
        print("Run command")

    def cmdHelp(self, arg):
        print("Help command")

    def cmdQuit(self, arg):
        self.running = False

    def cmdCreate(self, arg):
        try:
            if self.user.getPermission() <= 1:
                if arg[0].upper() == "USER":
                    self.cmdCreateUser()
                    return 0
        except:
            pass
        self.printerInvCmd(["Create"] + arg)

    def cmdLogin(self, arg):
        if self.user != self.defaultUser:
            self.cmdLogout(arg)
        pass

    def cmdLogout(self, arg):
        if self.user != self.defaultUser:
            valid = False
            while not valid:
                self.printer("Are you sure you want to log out of user: " + self.user.getName())
                ans = input()
                if ans.upper() == "YES":
                    self.user = self.defaultUser
                    self.printer("Logged out of user: " + self.user.getName()) 
                    valid = True
                elif ans.upper() == "NO" or ans.upper() == "CANCEL":
                    valid = True
                else:
                    self.printerInvIn(ans, "enter Yes or No")
            

    def cmdCreateUser(self):
        cancelled = False
        attributes = ["username", "password", "permission", "speed (Default 25)"]
        values = []
        count = 0
        while count < 4 and not cancelled:
            error = None
            self.printer("Please enter the new users " + attributes[count] + ": ")
            ans = input()
            if ans.upper() == "CANCEL":
                cancelled = True
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
                if Utilities.isInt(ans):
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
                if Utilities.isInt(ans):
                    ans = int(ans)
                    values.append(ans)
                    count += 1
                else:
                    error = "a valid number"
            if error != None:
                self.printerInvIn(ans, error)
        if not cancelled:
            self.createUser(values)
                
                        

    def initializeCommands(self):
        self.commands = {}
        self.commands["RUN"] = self.cmdRun
        self.commands["QUIT"] = self.cmdQuit
        self.commands["EXIT"] = self.cmdQuit
        self.commands["HELP"] = self.cmdHelp
        self.commands["CREATE"] = self.cmdCreate
        self.commands["LOGIN"] = self.cmdLogin
