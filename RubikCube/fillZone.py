import numpy as np
import random
from RubikCube.tile import tile

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}


class Grid:
    def __init__(self, N, colors):
        self.N = N
        self.grid = []
        self.playerCells = []
        self.colorList = dict(colors)
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    self.grid.append(tile(i, j, random.choice(list(self.colorList.values())), True))
                    self.playerCells.append(self.grid[i+j*N])
                    self.grid[i+j*N].setIsPlayer(True)
                else:
                    self.grid.append(tile(i, j, random.choice(list(self.colorList.values())), False))

        self.addNeighBors()

    def printState(self):
        data = np.zeros((self.N, self.N), dtype=int)
        for i in range(self.N ):
            for j in range(self.N):
                data[i][j] = self.grid[i + j * self.N].tileColor

        for i in range(self.N):
            print(data[i])


    def changeColor(self, color):
        colorToChange = self.colorList[color]
        for i in range(self.N * self.N):
            if self.grid[i].isPlayer:
                self.grid[i].tileColor = colorToChange
        self.addNeighBors()

    # def includeCells(self,cell):
    def isSolved(self):
        return len(self.playerCells) == self.N * self.N
    def addNeighBors(self):
        for cell in self.playerCells:
            if cell.hasTop(self.N):
                top = self.grid[cell.x + (cell.y+1)*self.N]
                if not top.getIsPlayer() and cell.hasSameColor(top):
                    top.setIsPlayer(True)
                    self.playerCells.append(top)
            if cell.hasRight(self.N):
                right = self.grid[cell.x+1+cell.y*self.N]
                if not right.getIsPlayer() and cell.hasSameColor(right):
                    right.setIsPlayer(True)
                    self.playerCells.append(right)
            if cell.hasDown():
                down = self.grid[cell.x + (cell.y-1)*self.N]
                if not down.getIsPlayer() and cell.hasSameColor(down):
                    down.setIsPlayer(True)
                    self.playerCells.append(down)
            if cell.hasLeft():
                left = self.grid[cell.x-1+cell.y*self.N]
                if not left.getIsPlayer() and cell.hasSameColor(left):
                    left.setIsPlayer(True)
                    self.playerCells.append(left)




