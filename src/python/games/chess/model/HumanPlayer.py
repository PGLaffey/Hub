from Player import Player

class HumanPlayer(Player):

    def __init__(self, game, num):
        self.command = {
            "move": self.move,
            "moves": self.moves,
            "save": self.save,
            "help": self.chelp,
            "print": self.cprint
            }
        self.converter = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7}
        super().__init__(game, num)

    def takeTurn(self):
        self.pieces = self.game.getPieces(self.num)
        done = False
        while not done:
            arg = input("Enter command: ").lower().split(" ")
            cmd = arg.pop(0)
            if cmd in self.command:
                done = self.command.get(cmd)(arg)
            else:
                print("Invalid command, type Help for assistance.")

    def move(self, arg):
        if len(arg) > 1:
            if len(arg) == 3:
                arg.pop(1)
            if self.validLocation(arg[0]):
                if self.validLocation(arg[1]):
                    piece = self.findPiece(arg[0])
                    if piece:
                        self.moveTo(piece, arg[1])
                        return True
        while True:
            loc1 = input("Enter the location of the piece you want to move: ")
            if loc1.lower() == "cancel":
                return False
            if self.validLocation(loc1) and self.findPiece(loc1):
                break
        piece = self.findPiece(loc1)
        while True:
            loc2 = input("Enter the location you want to move the piece to: ")
            if loc2.lower() == "cancel":
                return False
            if self.validLocation(loc2) and self.validMove(loc2, piece):
                break
        self.moveTo(piece, loc2)
        return True

    def findPiece(self, loc):
        coord = (self.converter[loc[0].lower()], int(loc[1]) - 1)
        for piece in self.pieces:
            if piece.getLocation() == coord:
                return piece
        print("You do not have a piece at the location " + str(loc))
        return False

    def moveTo(self, piece, newLoc):
        coord = (self.converter[newLoc[0].lower()], int(newLoc[1]) - 1)
        piece.move(coord)
        self.game.checkAttack(piece)

    def validMove(self, loc, piece):
        coord = (self.converter[loc[0].lower()], int(loc[1]) - 1)
        if coord in piece.getMoves():
            return True
        return False

    def validLocation(self, loc):
        if loc[0].lower() in self.converter:
            if int(loc[1]) <= 8 and int(loc[1]) >= 1:
                return True
        print("Location " + loc + " is invalid. Please enter between A1 and H8.")
        return False

    def cprint(self, arg):
        self.game.printBoard()

    def save(self):
        pass

    def chelp(self):
        pass

    def moves(self, arg):
        if len(arg) > 0:
            loc = arg.pop(0)
            if validLocation(loc) and findPiece(ans):
                piece = findPiece(ans)
                print("Moves for " + piece.__repr__() + " at " + loc + ":")
                print("| ", end='')
                for move in piece.getMoves():
                    print(str(move[0]) + ", " + str(move[1]) + " | ")
                return False
        while True:
            print("Enter the location of the piece you want to check the moves for:")
            ans = input()
            if validLocation(ans) and findPiece(ans):
                piece = findPiece(ans)
                print("Moves for " + piece.__repr__() + " at " + loc + ":")
                print("| ", end='')
                for move in piece.getMoves():
                    print(str(move[0]) + ", " + str(move[1]) + " | ")
                return False
            
