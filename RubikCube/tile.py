class tile:

    def __init__(self, x, y, type, tilecolor, neighbors):
        self.x = x
        self.y = y
        self.type = type
        self.TileColor = tilecolor
        self.neighbors = neighbors

    def getNeighbors(self):
        return self.neighbors

    def setColor(self, color):
        self.color = color

    def hasSameColor(self, Tile):
        if self.TileColor == Tile.TileColor:
            return True
        return False
