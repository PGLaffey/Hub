from model.Board import Board, ROWS

class Chess():
    def __init__(self):
        self.board = Board()
        self.win = None
        
        self.setup()

    def setup(self):
        print("Welcome to Chess, type 'Start' to play.")
        while (input().lower() != "start"):
            pass
        self.running()

    def running(self):
        while self.win == None:
            self.playerTurn()
            if not self.win:
                self.aiTurn()

    def playerTurn(self):
        self.board.toString()
        print("Type 'move yx' where y is A to H and x is 1 to 8.")
        command = ""
        while self.invalidCommand(command):
            command = input()
            print("Invalid Command")
        words = command.split(' ')
        piece = self.board.get(words[1])
        print(piece.toString())
        

    def invalidCommand(self, command):
        try:
            words = command.split(' ')
            if words[0] != "move":
                return True
            if words[2] != "to":
                return True
            if not isCoords(words[1]):
                return True
            if not isCoords(words[3]):
                return True
            return False
        except:
            return True

    def isCoords(self, coords):
        if coords[0] in ROWS:
            if coords[1] in range(8):
                return True
        return False
        

    def aiTurn(self):
        pass

Chess()
