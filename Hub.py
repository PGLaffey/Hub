import time

class Hub():
    def __init__(self):
        self.db = Database()
        self.user = None
        self.user = self.login("DEFAULT", "PASSWORD")

    def login(self, username, password):
        users = self.db.getUsers()
        for user in users:
            if user.getUsername() == username:
                if user.getPassword() == password:
                    self.printer("Logged into user: " + username)
                    return user
        self.printer("Invalid login credentials.")

    def printer(self, string):
        for char in string:
            print(char, end="")
            if self.user != None:
                time.sleep(self.user.getSpeed())
            else:
                time.sleep(0.1)

class Database():
    def __init__(self):
        self.importUsers()
    
    def importUsers(self):
        self.users = []
        self.users.append(User("DEFAULT", "PASSWORD", 1))

    def getUsers(self):
        return self.users

class User():
    def __init__(self, username, password, permission):
        self.username = username
        self.password = password
        self.permission = permission
        self.speed = 0.01

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getPermission(self):
        return self.permission

    def getSpeed(self):
        return speed

    def setSpeed(self, speed):
        self.speed = speed

    def setPermission(self, permission):
        self.permission = permission

    def setPassword(self, password):
        self.password = password

Hub()
    
