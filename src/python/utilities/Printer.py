import time
import sys

user = None

def printerSetUser(newUser):
    global user
    user = newUser

def printer(string):
    global user
    for char in string:
        print(char, end="")
        if user != None:
            time.sleep(1/user.getSpeed())
        else:
            time.sleep(1/25)

def printerInvCmd(arg):
    printer(" ".join(arg) + " is not a valid command. Type 'help' for assistance.\n")

def printerInvInput(response, valid):
    printer("Invalid input: " + response + "\nPlease enter " + valid + ".\n")

def printerLog(log):
    global user
    for char in string:
        print(char, end="", file=sys.err)
        if user != None:
            time.sleep(1/user.getSpeed())
        else:
            time.sleep(1/25)
    print()
