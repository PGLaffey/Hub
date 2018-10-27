from Piece import Piece

class Queen(Piece):
    def __init__(self, location, team):
        super().__init__(location, team)

    def __str__(self):
        return "Q"

    def __repr__(self):
        return "Q"

    def getMoves(self):
        for d in range(8):
            if location[0] + d < 8:
                yield (location[0] + d, location[1])
                if location[1] + d < 8:
                    yield (location[0] + d, location[1] + d)
                elif location[1] - d >= 0:
                    yield (location[0] + d, location[1] - d)
            if location[0] - d >= 0:
                yield (location[0] - d, location[1])
                if location[1] + d < 8:
                    yield (location[0] - d, location[1] + d)
                elif location[1] - d >= 0:
                    yield (location[0] - d, location[1] - d)
            if location[1] + d < 8:
                yield (location[0], location[1] + d)
            if location[1] - d >= 0:
                yield (location[0], location[1] - d)
