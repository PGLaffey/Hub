import mysql.connector
from model.User import User

class Database():
    def __init__(self):
        self.connect, self.cursor = self.getConnection()
        self.importUsers()

    def getConnection(self):
        config = {
            'user': 'user',
            'password': 'plaffa',
            'host': '127.0.0.1',
            'port': '3306',
            'raise_on_warnings': True,
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        try:
            connnection.database = "hub"
        except:
            createDatabase(cursor)
        return connection, cursor
    
    def createDatabase(self, cursor):
        tables = {}
        tables['users'] = (
            "CREATE TABLE 'tblUsers' ("
            "'username' char(15) NOT NULL UNIQUE, "
            "'password' char(20) NOT NULL, "
            "'permission' tinyint DEFAULT 1, "
            "'speed' tinyint DEFAULT 50, "
            "PRIMARY KEY(username))")
        
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'"
                .format("hub"))
            for name, command in TABLES.iteritems():
                cursor.execute(command)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def closeConnection(self):
        self.cursor.close()
        self.connect.close()

    def getPassword(self, username):
        query = ("SELECT password FROM tblUsers "
                 "WHERE username == %s")
        results = self.runQuery(query, (username))
        if len(results) > 0:
            return results[0][0]
        return None

    def getUser(self, username):
        query = ("SELECT * FROM tblUsers "
                 "WHERE username == %s")
        results = self.runQuery(query, (username))
        return self.importUser(results[0])

    def importUser(self, attr):
        return User(attr[0], attr[1], attr[2], attr[3])

    def addUser(self, attr):
        query = ("INSERT INTO tblUsers (username, password, permission, speed) "
                 "VALUES (%s, %s, %s, %s)")
        return runQuery(query, attr)

    def userExists(self, username):
        query = ("SELECT * FROM tblUsers "
                 "WHERE username == %s")
        results = self.runQuery(query, (username))
        return len(results) > 0

    def runQuery(self, query, params):
        params = tuple(params)
        if query.split(" ")[0].upper() == "SELECT":
            return self.runSelectQuery(query, params)
        elif query.split(" ")[0].upper() == "INSERT" or query.split(" ")[0].upper() == "UPDATE":
            self.runUpdateQuery(query, params)
            return True

    def runUpdateQuery(self, query, params):
        self.cursor.execute(query, params)
    
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
        self.users.append(User("DEFAULT", "PASSWORD", 1))

    def getUsers(self):
        return self.users
