class User():
    def __init__(self, username, password, permission, speed = 25):
        self.username = username
        self.password = password
        self.permission = permission
        self.speed = speed

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getPermission(self):
        return self.permission

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def setPermission(self, permission):
        self.permission = permission

    def setPassword(self, password):
        self.password = password
