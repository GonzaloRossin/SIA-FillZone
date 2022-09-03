import numpy as np
import random
import copy
from game.tile import tile

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}


class Grid:
    def __init__(self, N, colors):
        self.playerColor = None
        self.N = N
        self.grid = [[] for i in range(N)]
        self.playerCells = []
        self.nonControlled = []
        self.colorList = dict(colors)
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    newColor = random.choice(list(self.colorList.values()))
                    self.grid[i].append(tile(i, j, newColor, True))
                    self.playerColor = newColor
                    self.playerCells.append(self.grid[i][j])
                    self.grid[i][j].setIsPlayer(True)
                else:
                    Tile = tile(i, j, random.choice(list(self.colorList.values())), False)
                    self.grid[i].append(Tile)
                    self.nonControlled.append(Tile)

        self.addNeighBors()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.playerColor != other.playerColor or len(self.playerCells) != len(other.playerCells):
            return False
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True

    def __hash__(self):
        return hash((len(self.playerCells), self.playerColor))

    def printState(self):
        data = np.zeros((self.N, self.N), dtype=int)
        for i in range(self.N):
            for j in range(self.N):
                data[i][j] = self.grid[i][j].getColor()

        for i in range(self.N):
            print(data[i])

    def changeColor(self, color):
        colorToChange = self.colorList[color]
        self.playerColor = colorToChange
        for cell in self.playerCells:
            cell.setColor(colorToChange)

        self.addNeighBors()

    def getPlayerColor(self):
        return self.playerColor

    def isSolved(self):
        return len(self.playerCells) == self.N * self.N

    def addNeighBors(self):
        for cell in self.playerCells:
            if cell.hasTop():
                top = self.grid[cell.x - 1][cell.y]
                if not top.getIsPlayer() and cell.hasSameColor(top):
                    top.setIsPlayer(True)
                    self.playerCells.append(top)
                    self.nonControlled.remove(top)
            if cell.hasRight(self.N):
                right = self.grid[cell.x][cell.y + 1]
                if not right.getIsPlayer() and cell.hasSameColor(right):
                    right.setIsPlayer(True)
                    self.playerCells.append(right)
                    self.nonControlled.remove(right)
            if cell.hasDown(self.N):
                down = self.grid[cell.x + 1][cell.y]
                if not down.getIsPlayer() and cell.hasSameColor(down):
                    down.setIsPlayer(True)
                    self.playerCells.append(down)
                    self.nonControlled.remove(down)
            if cell.hasLeft():
                left = self.grid[cell.x][cell.y - 1]
                if not left.getIsPlayer() and cell.hasSameColor(left):
                    left.setIsPlayer(True)
                    self.playerCells.append(left)
                    self.nonControlled.remove(left)

    def getStateCopy(self):
        return copy.deepcopy(self)

    def getPlayerCount(self):
        return len(self.playerCells)

    def getColorValue(self, colorName):
        return self.colorList[colorName]

    def getColorDict(self):
        return self.colorList

    def getGrid(self):
        return self.grid

    def getUncontrolledTiles(self):
        return self.nonControlled
