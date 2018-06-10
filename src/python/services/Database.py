import sqlite3
from os.path import dirname, abspath
from ..model.User import User

class Database():
    def __init__(self):
        self.connect, self.cursor = self.getConnection()
        self.importUsers()

    def getConnection(self):
        srcDir = dirname(dirname(__file__))
        connection = sqlite3.connect(srcDir  + "\\Database\\hub")
        cursor = connection.cursor()
        if not self.tablesExisit(cursor):
            self.createDatabase(cursor)
        return connection, cursor

    def tablesExisit(self, cursor):
        allTables = ["tblUsers"]
        dbTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for table in dbTables:
            if table[0] in allTables:
                allTables.remove(table[0])
            else:
                return False
        if len(allTables) == 0:
            return True
        return False
    
    def createDatabase(self, cursor):
        tables = {}
        tables['users'] = (
            "CREATE TABLE 'tblUsers' ("
            "'username' char(15) NOT NULL UNIQUE, "
            "'password' char(20) NOT NULL, "
            "'permission' tinyint, "
            "'speed' tinyint, "
            "PRIMARY KEY(username))")
        
        for name, command in tables.items():
            cursor.execute(command)

    def closeConnection(self):
        self.cursor.close()
        self.connect.close()

    def getPassword(self, username):
        query = ("SELECT password FROM tblUsers "
                 "WHERE username = ?")
        results = self.runQuery(query, (username,))
        if len(results) > 0:
            return results[0][0]
        return None

    def getUser(self, username):
        query = ("SELECT * FROM tblUsers "
                 "WHERE username = ?")
        results = self.runQuery(query, (username,))
        return self.importUser(results[0])

    def importUser(self, attr):
        return User(attr[0], attr[1], attr[2], attr[3])

    def addUser(self, attr):
        query = ("INSERT INTO tblUsers (username, password, permission, speed) "
                 "VALUES (?, ?, ?, ?)")
        return self.runQuery(query, attr)

    def userExists(self, username):
        query = ("SELECT * FROM tblUsers "
                 "WHERE username = ?")
        results = self.runQuery(query, (username,))
        return len(results) > 0

    def runQuery(self, query, params):
        params = tuple(params)
        if query.split(" ")[0].upper() == "SELECT":
            return self.runSelectQuery(query, params)
        elif query.split(" ")[0].upper() == "INSERT" or query.split(" ")[0].upper() == "UPDATE":
            return self.runUpdateQuery(query, params)

    def runUpdateQuery(self, query, params):
        self.cursor.execute(query, params)
        self.connect.commit()
        return True
    
    def runSelectQuery(self, query, params):
        self.cursor.execute(query, params)
        results = []
        count = 0
        for row in self.cursor:
            results.append([])
            for column in row:
                results[count].append(column)
            count += 1
        return results
    
    def importUsers(self):
        self.users = []
        self.users.append(User("DEFAULT", "PASSWORD", 1, 25))

    def getUsers(self):
        return self.users
