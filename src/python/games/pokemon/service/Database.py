import sqlite3
import sys
from os.path import dirname, abspath
from python.games.pokemon.model import Pokemon
from python.utilities.Printer import *

class Database():
    def __init__(self):
        self.connect, self.cursor = self.getConnection()

    def getConnection(self):
        srcDir = dirname(dirname(dirname(dirname(__file__))))
        connection = sqlite3.connect(srcDir  + "\\database\\pokemon")
        cursor = connection.cursor()
        if not self.tablesExisit(cursor):
            self.createDatabase(cursor)
            connection.commit()
        return connection, cursor

    def tablesExisit(self, cursor):
        allTables = ["tblPokemon", "tblMoves"]
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
            "'defence' integer NOT NULL, "
            "'spattack' integer NOT NULL, "
            "'spdefence' integer NOT NULL, "
            "'speed' integer NOT NULL, "
            "'generation' integer NOT NULL, "
            "PRIMARY KEY(id))")
        tables['moves'] = (
            "CREATE TABLE IF NOT EXISTS 'tblMoves' ("
            "'id' integer PRIMARY KEY AUTOINCREMENT, "
            "'name' varchar(50) NOT NULL, "
            "'element' varchar(10) NOT NULL, "
            "'status' integer NOT NULL, "
            "'power' integer NOT NULL, "
            "'accuracy' integer NOT NULL, "
            "'uses' integer NOT NULL, "
            "'description' text, "
            "'generation' integer NOT NULL)")
        for name, command in tables.items():
            cursor.execute(command)
            printerLog("Created database table: " + name)
        self.createIndices(cursor)
        self.populateTables(cursor)

    def createIndices(self, cursor):
        indices = {}
        indices['pokemon'] = ("CREATE INDEX IF NOT EXISTS indexPkGen ON tblPokemon (generation)")
        indices['moves'] = ("CREATE INDEX IF NOT EXISTS indexMvGen ON tblMoves (generation)")
        for name, command in indices.items():
            cursor.execute(command)
            printerLog("Created database index: " + name)

    def populateTables(self, cursor):
        srcDir = dirname(dirname(dirname(dirname(__file__)))) + "\\resources\\pokemon"
        files = ["\\pokemon_gen_1", "\\moves_gen_1"]
        for file in files:
            if "pokemon" in file:
                self.populatePokemonTable(cursor, srcDir + file)
            elif "moves" in file:
                self.populateMovesTable(cursor, srcDir + file)

    def populateMovesTable(self, cursor, directory):
        filename = directory.split("\\").pop()
        printerLog("Loading " + filename)
        try:
            file = open(directory)
            header = file.readline()
            header = header.split(' ')
            if header[0] == "GEN":
                gen = int(header[1])
                for line in file:
                    if not line.startswith('#'):
                        line.strip('\n')
                        move = line.split(',')
                        query = ("INSERT INTO tblMoves "
                                 "(name, element, status, power, accuracy, "
                                 "uses, description, generation) "
                                 "VALUES (")
                        attr = 0
                        while attr < len(move):
                            if attr == 1:
                                query += "'" + move[attr].upper() + "',"
                            elif attr == 2:
                                power = move[attr]
                                if power == '—':
                                    query += "1,0,"
                                else:
                                    query += "0," + power + ","
                            elif attr == 3:
                                accur = move[attr]
                                if accur == '—':
                                    query += "-1,"
                                else:
                                    query += accur + ","
                            elif attr == 4:
                                query += move[attr] + ","
                            else:
                                query += "'" + move[attr] + "',"
                            attr += 1
                        query += str(gen) + ")"
                        cursor.execute(query)
                        print(query)
                printerLog("Loading " + filename + " Complete")
            else:
                raise ValueError
        except IOError:
            printerLog("Failed to load file: " + directory)
        except ValueError:
            printerLog("Bad file format: " + directory)
        
    def populatePokemonTable(self, cursor, directory):
        filename = directory.split("\\").pop()
        printerLog("Loading " + filename)
        try:
            file = open(directory)
            header = file.readline()
            header = header.split(' ')
            if header[0] == "GEN":
                gen = int(header[1])
                for line in file:
                    if not line.startswith('#'):
                        line.strip('\n')
                        pm = line.split(',')
                        query = ("INSERT INTO tblPokemon "
                                 "(id, name, element1, element2, total, health,"
                                 " attack, defence, spattack, spdefence, speed,"
                                 " generation) VALUES (")
                        attr = 0
                        while attr < len(pm):
                            if attr == 1:
                                name = pm[attr]
                                query += "'" + name + "', "
                            elif attr == 2:
                                types = pm[attr].split(' ')
                                query += "'" + types[0].upper() + "', "
                                if len(types) > 1:
                                    query += "'" + types[1].upper() + "', "
                                else:
                                    query += "NULL, "
                            else:
                                query += pm[attr] + ", "
                            attr += 1
                        query += str(gen) + ")"
                        cursor.execute(query)
                printerLog("Loading " + filename + " Complete")
            else:
                raise ValueError
        except IOError:
            printerLog("Failed to load file: " + directory)
        except ValueError:
            printerLog("Bad file format: " + directory)
                             
    def closeConnection(self):
        self.cursor.close()
        self.connect.close()

    def getNames(self, gen, elements):
        pokemonNames = {}
        query = "SELECT id, name FROM tblPokemon"
        if str(gen) != '0':
            query += " WHERE generation <= " + str(gen)
            if len(elements) > 0:
                query += (" AND element1 = '" + elements[0] + "' OR " +
                          "generation <= " + str(gen) + " AND element2 = '" + elements[0] + "'")
                elements.pop(0)
                for element in elements:
                    query += (" OR generation <= " + str(gen) + " AND element1 = '" + element +
                              "' OR generation <= " + str(gen) + " AND element2 = '" + element + "'")
        else:
            if len(elements) > 0:
                query += (" WHERE element1 = '" + elements[0] +
                          "' OR element2 = '" + elements[0] + "'")
                elements.pop(0)
                for element in elements:
                    query += (" OR element1 = '" + element + "' OR element2 = '" + element + "'")                
        allPokemon = self.cursor.execute(query)
        for pmID, name in allPokemon:
            pokemonNames[pmID] = name
        return pokemonNames

    def loadPokemonAttr(self, pmID):
        try:
            return self.cursor.execute(("SELECT * FROM tblPokemon "
                                        "WHERE id = " + str(pmID))).fetchall()[0]
        except IndexError:
            printerLog("No Pokemon found with ID: " + str(pmID))
                                        
        
