class tile:

    def __init__(self, x, y, tilecolor, isPlayer):
        self.x = x
        self.y = y
        self.isPlayer = isPlayer
        self.tileColor = tilecolor

    def setColor(self, tilecolor):
        self.tileColor = tilecolor

    def hasSameColor(self, Tile):
        if self.tileColor == Tile.tileColor:
            return True
        return False

    def setIsPlayer(self, isPlayer):
        self.isPlayer = isPlayer

    def getIsPlayer(self):
        return self.isPlayer

    def hasRight(self, maxValueX):
        return self.x < maxValueX - 1

    def hasTop(self, maxValueY):
        return self.y < maxValueY - 1

    def hasLeft(self):
        return self.x > 0

    def hasDown(self):
        return self.y > 0
