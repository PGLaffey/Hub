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

Hub()
    
