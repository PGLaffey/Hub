from random import randint

def attempt_escape():
    num = randint(1,100)
    if num < 25:
        return True
    else:
        return False
