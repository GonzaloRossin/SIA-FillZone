from RubikCube.CubeSide import CubeSide


class Cube:

    def __init__(self, N):
        self.N = N
        self.front = CubeSide(N, 'G', 'F')
        self.left = CubeSide(N, 'O', 'L')
        self.right = CubeSide(N, 'R', 'R')
        self.up = CubeSide(N, 'W', 'U')
        self.down = CubeSide(N, 'Y', 'D')
        self.back = CubeSide(N, 'B', 'B')

    def rotateRowRight(self, rowIndex):
        rowToCopy1 = self.right.getRow(rowIndex)
        self.right.setRow(self.front.getRow(rowIndex), rowIndex)
        rowToCopy2 = self.back.getRow(rowIndex)
        self.back.setRow(rowToCopy1, rowIndex)
        rowToCopy1 = self.left.getRow(rowIndex)
        self.left.setRow(rowToCopy2, rowIndex)
        self.front.setRow(rowToCopy1, rowIndex)

    def rotateRowLeft(self, rowIndex):
        rowToCopy1 = self.left.getRow(rowIndex)
        self.left.setRow(self.front.getRow(rowIndex), rowIndex)
        rowToCopy2 = self.back.getRow(rowIndex)
        self.back.setRow(rowToCopy1, rowIndex)
        rowToCopy1 = self.right.getRow(rowIndex)
        self.right.setRow(rowToCopy2, rowIndex)
        self.front.setRow(rowToCopy1, rowIndex)

    def rotateColUp(self, colIndex):
        col1 = self.up.getCol(colIndex)
        self.up.setCol(self.front.getCol(colIndex), colIndex)
        col2 = self.back.getCol(colIndex)
        self.back.setCol(col1, colIndex)
        col1 = self.down.getCol(colIndex)
        self.down.setCol(col2, colIndex)
        self.front.setCol(col1, colIndex)

    def rotateColDown(self, colIndex):
        col1 = self.down.getCol(colIndex)
        self.down.setCol(self.front.getCol(colIndex),colIndex)
        col2 = self.back.getCol(colIndex)
        self.back.setCol(col1,colIndex)
        col1 = self.up.getCol(colIndex)
        self.up.setCol(col2,colIndex)
        self.front.setCol(col1,colIndex)

    def cPerspectiveUp(self):
        side1 = self.up
        self.up =self.front
        side2 = self.back
        self.back = side1
        side1 = self.down
        self.down = side2
        self.front = side1

    def cPerspectiveDown(self):
        side1 = self.down
        self.down = self.front
        side2 = self.back
        self.back = side1
        side1 = self.up
        self.up = side2
        self.front = side1

    def cPerspectiveLeft(self):
        side1 = self.left
        self.left = self.front
        side2 = self.back
        self.back = side1
        side1 = self.right
        self.right = side2
        self.front = side1

    def cPerspectiveRight(self):
        side1 = self.right
        self.right = self.front
        side2 = self.back
        self.back = side1
        side1 = self.left
        self.left = side2
        self.front = side1

    def printCube(self):
        print("front:")
        self.front.printSide()
        print("left:")
        self.left.printSide()
        print("right:")
        self.right.printSide()
        print("up:")
        self.up.printSide()
        print("down:")
        self.down.printSide()
        print("back:")
        self.back.printSide()
