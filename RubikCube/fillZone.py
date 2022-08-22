import numpy as np
import random
from RubikCube.TileType import TyleType
from RubikCube.tile import tile

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}


class Grid:
    def __init__(self, N, colors):
        self.N = N
        self.grid = []
        self.colorList = dict(colors)
        self.player = []
        self.player.append(tile(0, 0, TyleType.TOP_LEFT_CORNER, random.choice(list(self.colorList.values())), 2))
        for i in range(N):
            for j in range(N):
                if i == 0:
                    if j == 0:
                        self.grid.append(
                            tile(i, j, TyleType.BOTTOM_LEFT_CORNER, random.choice(list(self.colorList.values())), 2))
                    elif j < N - 1:
                        self.grid.append(tile(i, j, TyleType.BOTTOM_EDGE, random.choice(list(self.colorList.values())), 3))
                    else:
                        self.grid.append(
                            tile(i, j, TyleType.BOTTOM_RIGHT_CORNER, random.choice(list(self.colorList.values())), 2))
                elif i < N - 1:
                    if j == 0:
                        self.grid.append(
                            tile(i, j, TyleType.LEFT_EDGE, random.choice(list(self.colorList.values())), 3))
                    elif j < N - 1:
                        self.grid.append(
                            tile(i, j, TyleType.INNER_CELL, random.choice(list(self.colorList.values())), 4))
                    else:
                        self.grid.append(
                            tile(i, j, TyleType.RIGHT_EDGE, random.choice(list(self.colorList.values())), 3))
                else:
                    if j == 0:
                        self.grid.append(
                            tile(i, j, TyleType.TOP_LEFT_CORNER, random.choice(list(self.colorList.values())), 2))
                    elif j < N - 1:
                        self.grid.append(
                            tile(i, j, TyleType.TOP_EDGE, random.choice(list(self.colorList.values())), 3))
                    else:
                        self.grid.append(
                            tile(i, j, TyleType.TOP_RIGHT_CORNER, random.choice(list(self.colorList.values())), 2))

    def printState(self):
        data = np.zeros((self.N, self.N), dtype=int)
        for i in range(self.N-1,-1,-1):
            for j in range(self.N-1,-1,-1):
                data[i][j] = self.grid[i + j * 14].TileColor

        for i in range(14):
            print(data[i])

    def checkTileNeighbors(self, Tile):
        same_color = 0
        if Tile.TyleTipe.TyleType.TOP_LEFT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[
                Tile.x + self.N * (Tile.y + 1)].color:  # cell bellow
                same_color += 1

        elif Tile.TyleTipe.TyleType.TOP_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + 1 + self.N * Tile.y].color:  # cell to the right
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[ Tile.x - 1 + self.N * Tile.y].color:  # cell to the left
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y + 1)].color:  # cell bellow
                same_color += 1

        elif Tile.TyleTipe.TyleType.TOP_RIGHT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x - 1 + self.N * Tile.y].color:  # cell to the left
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y + 1)].color:  # cell on
                same_color += 1

        elif Tile.TyleTipe.TyleType.LEFT_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + 1 + self.N * Tile.y].color:  # check if [1][0] or [0][1] have same color
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y + 1)].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1

        elif Tile.TyleTipe.TyleType.RIGHT_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y + 1)].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x - 1 + self.N * Tile.y].color:
                same_color += 1

        elif Tile.TyleTipe.TyleType.BOTTOM_LEFT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + 1 + self.N * Tile.y].color:
                same_color += 1

        elif Tile.TyleTipe.TyleType.BOTTOM_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + 1 + self.N * Tile.y].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x - 1 + self.N * Tile.y].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1

        elif Tile.TyleTipe.TyleType.BOTTOM_RIGHT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x - 1 + self.N * Tile.y].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1

        elif Tile.TyleTipe.TyleType.INNER_CELL:
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x - 1 + self.N * Tile.y].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y - 1)].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + 1 + self.N * Tile.y].color:
                same_color += 1
            if self.grid[Tile.x + self.N * Tile.y].color == self.grid[Tile.x + self.N * (Tile.y + 1)].color:
                same_color += 1

        return same_color

    def checkNeighbors(self):
        color_count = {}
        for tile in self.player:
            neighbors = self.checkTileNeighbors(tile)
            color_count[self.grid[tile.x][tile.y]] += neighbors

    def changeColor(self, color):
        colorToChange = self.colorList[color]
        for cell in self.player:
            self.grid[cell.x+cell.y*self.N].TileColor = colorToChange
            if cell.getNeighbors() > 0:
                self.addNeighBors(cell, self.player)


    def addNeighBors(self, Tile, listToAdd):
        if Tile.type == TyleType.TOP_LEFT_CORNER:
            if  self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell bellow
                cell = self.grid[Tile.x + (Tile.y + 1) * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
        elif Tile.type == TyleType.TOP_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[ Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell bellow
                cell = self.grid[Tile.x + (Tile.y + 1) * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

        elif Tile.type == TyleType.TOP_RIGHT_CORNER:

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y -1)]):  # cell bellow
                cell = self.grid[Tile.x + (Tile.y + 1) * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

        elif Tile.type == TyleType.LEFT_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y - 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell bellow
                cell = self.grid[Tile.x + (Tile.y + 1) * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
        elif Tile.type == TyleType.RIGHT_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y - 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell bellow
                cell = self.grid[Tile.x + (Tile.y + 1) * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

        elif Tile.type == TyleType.BOTTOM_LEFT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

        elif Tile.type == TyleType.BOTTOM_EDGE:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

        elif Tile.type == TyleType.BOTTOM_RIGHT_CORNER:
            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
        else:

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x - 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y - 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + 1 + self.N * Tile.y]):  # cell to the right
                cell = self.grid[Tile.x + 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return

            if self.grid[Tile.x + self.N * Tile.y].hasSameColor(self.grid[Tile.x + self.N * (Tile.y + 1)]):  # cell to the right
                cell = self.grid[Tile.x - 1 + Tile.y * self.N]
                cell.neighbors -= 1
                Tile.neighbors -= 1
                listToAdd.append(cell)
                if Tile.neighbors == 0:
                    return
