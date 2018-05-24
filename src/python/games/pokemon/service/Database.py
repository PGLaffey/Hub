import sqlite3
from os.path import dirname, abspath

class Database():
    def __init__(self):
        self.connect, self.cursor = self.getConnection()

    def getConnection(self):
        srcDir = dirname(dirname(dirname(dirname(__file__))))
        connection = sqlite3.connect(srcDir  + "\\Database\\pokemon")
        cursor = connection.cursor()
        if not self.tablesExisit(cursor):
            self.createDatabase(cursor)
        return connection, cursor

    def tablesExisit(self, cursor):
        allTables = ["tblPokemon", "tblMoves"]
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
        tables['pokemon'] = (
            "CREATE TABLE IF NOT EXISTS 'tblPokemon' ("
            "'id' integer NOT NULL UNIQUE, "
            "'name' varchar(50) NOT NULL, "
            "'element1' varchar(10) NOT NULL, "
            "'element2' varchar(10) NOT NULL, "
            "'total' integer NOT NULL, "
            "'health' integer NOT NULL, "
            "'attack' integer NOT NULL, "
            "'defence' integer NOT NULL, "
            "'spattack' integer NOT NULL, "
            "'spdefence' integer NOT NULL, "
            "'speed' integer NOT NULL, "
            "PRIMARY KEY(id))")
        
        for name, command in tables.items():
            cursor.execute(command)

    def closeConnection(self):
        self.cursor.close()
        self.connect.close()
