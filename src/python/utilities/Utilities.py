def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
