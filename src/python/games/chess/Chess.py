from model.Game2P import Game2P
from model.HumanPlayer import HumanPlayer
from model.AIPlayer import AIPlayer

class Chess(object):
    def __init__(self):
        self.welcomeMessage()
        numPlayers = self.chooseNumPlayers()
        self.game = self.initializeGame(numPlayers)
        self.players = self.choosePlayers(numPlayers)
        self.play()

    def play(self):
        count = 0
        while True:
            print("It is player " + str(count + 1) + "'s turn.")
            self.game.printBoard()
            self.players[count].takeTurn()
            count += 1
            if count > len(self.players):
                count = 0

    def initializeGame(self, numPlayers):
        if numPlayers == 2:
            return Game2P()

    def chooseNumPlayers(self):
        ans = 0
        while ans < 2:
            try:
                ans = int(input("How many players? "))
                if ans < 2:
                    print("Number must be greater than 2.")
            except ValueError:
                ans = 0
                print("Please enter a number.")
        return ans

    def choosePlayers(self, numPlayers):
        players = []
        validYes = ["Y", "YES"]
        validNo = ["N", "NO"]
        count = 0
        while count < numPlayers:
            playerType = input("Is player " + str(count + 1) + " a human player? ").upper()
            if playerType in validYes:
                players.append(HumanPlayer(self.game, count + 1))
                count += 1
            elif playerType in validNo:
                players.append(AIPlayer(self.game, count + 1))
                count += 1
            else:
                print("Invalid answer. Please enter Yes or No.")
        return players
        
    def welcomeMessage(self):
        print("-----Welcome To Chess-----")

Chess()
