colordict = {"R": 0, "B": 1, "G": 2, "Y": 3, "W": 4, "O": 5}
facedict = {"F": 0, "L": 1, "R": 2, "U": 3, "D": 4, "B": 5}


class CubeSide:
    def __init__(self, N, color, side):
        self.matrix = [[colordict[color] for _ in range(N)] for _ in range(N)]
        self.position = facedict[side]
        self.size = N

    def getRow(self, rowIndex):
        return self.matrix[rowIndex]

    def setRow(self, row, rowIndex):
        self.matrix[rowIndex] = row

    def getCol(self, colIndex):
        col = []
        for i in range(self.size):
            col.append(self.matrix[i][colIndex])
        return col

    def setCol(self, col, colIndex):
        for i in range(self.size):
            self.matrix[i][colIndex] = col[i]

    def printSide(self):
        for j in range(self.size):
            print(self.matrix[j])
