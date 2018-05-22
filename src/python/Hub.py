import time
from python.services.Database import Database
from python.model.User import User

class Hub():
    def __init__(self):
        """
        Initializes the Hub program.
        """
        self.db = Database()
        self.running = True
        self.initializeCommands()
        self.user = None
        self.createUser("DEFAULT", "PASSWORD")
        self.user = self.attemptLogin("DEFAULT", "PASSWORD")
        self.getCommand()

    def getCommand(self):
        """
        Loops while the program is to continue running.
        - Asks for user input for the next command to run.
        - Runs the command if valid.
        - Restarts loop if program is to continue.
        """
        while self.running:
            self.printer("Command: ")
            command = input()
            self.processCommand(command)
        self.printer("Goodbye! :)")
        exit(0)

    def processCommand(self, command):
        """
        Takes a user input command as a string and turns it into a list of
        strings, split on spaces.
        Uses the first string to determine which command to run.
        """
        command = command.split(" ")
        if command[0].upper() in self.commands:
            self.commands[command.pop(0).upper()](command)
        else:
            self.printerInvCmd(command)
            

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
        """
        Attempts to log into a user from the username and password.
        If successful returns the user, otherwise returns None.
        @param username - The username of the user.
        @param password - The password of the user.
        @return         - The user if valid username and password, None otherwise.
        """
        if password == self.db.getPassword(username):
            self.printer("Logged into user: " + username + "\n")
            return self.db.getUser(username)
        self.printer("Invalid login credentials.\n")
        return None

    def printerInvCmd(self, arg):
        """
        Prints a invalid command message using the printer.
        @param arg - A list of the space seperated command string.
        """
        self.printer(" ".join(arg) + " is not a valid command. Type 'help' for assistance\n")

    def printer(self, string):
        """
        Prints the string to the console at the users type speed.
        If no user is logged in, it prints at the standard speed.
        @param string - The string to print.
        """
        for char in string:
            print(char, end="")
            if self.user != None:
                time.sleep(1/self.user.getSpeed())
            else:
                time.sleep(1/25)

    def cmdCreateUser():
        pass
    
                
    def cmdRun(self, arg):
        print("Run command")

    def cmdHelp(self, arg):
        print("Help command")

    def cmdQuit(self, arg):
        self.running = False

    def cmdCreate(self, arg):
        try:
            if self.user.getPermission() <= 1:
                if arg[0].upper == "USER":
                    self.cmdCreateUser()
                    return 0
        except:
            pass
        self.printerInvCmd(["Create"] + arg) 

    def initializeCommands(self):
        self.commands = {}
        self.commands["RUN"] = self.cmdRun
        self.commands["QUIT"] = self.cmdQuit
        self.commands["EXIT"] = self.cmdQuit
        self.commands["HELP"] = self.cmdHelp
        self.commands["CREATE"] = self.cmdCreate
