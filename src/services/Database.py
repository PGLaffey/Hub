class Database():
    def __init__(self):
        self.importUsers()
    
    def importUsers(self):
        self.users = []
        self.users.append(User("DEFAULT", "PASSWORD", 1))

    def getUsers(self):
        return self.users
