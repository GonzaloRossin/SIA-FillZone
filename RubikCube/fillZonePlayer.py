from RubikCube.tile import tile


class Player:
    def __init__(self):
        self.tiles = []
        self.tiles.append(tile(0, 0))

    def getNeighbors(self):
        return self.neighbors
