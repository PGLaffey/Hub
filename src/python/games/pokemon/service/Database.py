import sqlite3
import sys
from os.path import dirname, abspath
from model.Pokemon import Pokemon

class Database():
    def __init__(self):
        self.connect, self.cursor = self.getConnection()

    def getConnection(self):
        srcDir = dirname(dirname(dirname(dirname(__file__))))
        connection = sqlite3.connect(srcDir  + "\\database\\pokemon")
        cursor = connection.cursor()
        if not self.tablesExisit(cursor):
            self.createDatabase(cursor)
        return connection, cursor

    def tablesExisit(self, cursor):
        allTables = ["tblPokemon"]
        dbTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
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
            "'element2' varchar(10), "
            "'total' integer NOT NULL, "
            "'health' integer NOT NULL, "
            "'attack' integer NOT NULL, "
            "'defense' integer NOT NULL, "
            "'spattack' integer NOT NULL, "
            "'spdefence' integer NOT NULL, "
            "'speed' integer NOT NULL, "
            "'generation' integer NOT NULL, "
            "PRIMARY KEY(id))")
        for name, command in tables.items():
            cursor.execute(command)
            print("Created database table: " + name, file=sys.stderr)
        self.createIndices(cursor)
        self.populateTables(cursor)

    def createIndices(self, cursor):
        indices = {}
        indices['pokemon'] = ("CREATE INDEX indexPkGen ON tblPokemon (generation)")

        for name, command in indices.items():
            cursor.execute(command)
            print("Created database index: " + name, file=sys.stderr)

    def populateTables(self, cursor):
        srcDir = dirname(dirname(dirname(dirname(__file__)))) + "\\resources\\pokemon"
        self.populateGen1(cursor, srcDir)

    def populateGen1(self, cursor, srcDir):
        print("Loading generation 1 pokemon...", file=sys.stderr)
        try:
            file = open(srcDir + "\\pokemon_gen_1")
            header = file.readline()
            header = header.split(' ')
            if header[0] == "LENGTH":
                length = int(header[1])
                lineCount = 0
                for line in file:
                    if not line.startswith('#'):
                        line.strip('\n')
                        pm = line.split(',')
                        query = ("INSERT INTO tblPokemon "
                                 "(id, name, element1, element2, total, health,"
                                 " attack, defense, spattack, spdefence, speed,"
                                 " generation) VALUES (")
                        attr = 0
                        while attr < len(pm):
                            if attr == 1:
                                query += "'" + pm[attr] + "', "  
                            elif attr == 2:
                                types = pm[attr].split(' ')
                                query += "'" + types[0] + "', "
                                if len(types) > 1:
                                    query += "'" + types[1] + "', "
                                else:
                                    query += "NULL, "
                            else:
                                query += pm[attr] + ", "
                            attr += 1
                        query += "1)"
                        cursor.execute(query)
                    lineCount += 1
                    if lineCount % 10 == 0:
                        percentage = int((lineCount / length) * 100)
                        print("Loading Pokemon Gen 1 " + str(percentage) + "% Complete...", file=sys.stderr)
                print("Loading Pokemon Gen 1 100% Complete...", file=sys.stderr)
            else:
                raise ValueError
        except IOError:
            print("Failed to load file: " + srcDir + "\\pokemon_gen_1")
        except ValueError:
            print("Bad file format: " + srcDir + "\\pokemon_gen_1")
                             
    def closeConnection(self):
        self.cursor.close()
        self.connect.close()

    def getAllNames(self, generation):
        pokemonNames = {}
        allPokemon = self.cursor.execute("SELECT id, name FROM tblPokemon")
        for pmID, name in allPokemon:
            pokemonNames[name] = pmID
        return pokemonNames

    def loadPokemonAttr(self, pmID):
        try:
            return self.cursor.execute(("SELECT * FROM tblPokemon "
                                        "WHERE id = " + str(pmID))).fetchall()[0]
        except IndexError:
            print("No Pokemon found with ID: " + str(pmID ,file=sys.stderr)
                                        
        
