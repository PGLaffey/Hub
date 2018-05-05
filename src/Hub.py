import time
from services.Database import Database
from model.User import User

class Hub():
    def __init__(self):
        self.db = Database()
        self.createUser("DEFAULT", "PASSWORD")
        self.currentUser = self.attemptLogin("DEFAULT", "PASSWORD")

    def createUser(self, username, password, permission = 1, speed = 0.05):
        if not self.db.userExists(username):
            attr = list(username, password, permission, speed)
            self.db.addUser(attr)
            self.printer("User " + username + " successfully added.")
        else:
            self.printer("User " + username + " already exists.")

    def login(self):
        print("login")

    def attemptLogin(self, username, password):
        if password == self.db.getPassword(username):
            self.printer("Logged into user: " + username)
            return self.db.getUser(username)
        self.printer("Invalid login credentials.")

    def printer(self, string):
        for char in string:
            print(char, end="")
            if self.user != None:
                time.sleep(self.user.getSpeed())
            else:
                time.sleep(0.05)

Hub()
    
