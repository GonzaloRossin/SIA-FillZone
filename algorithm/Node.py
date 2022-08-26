class StateNode:

    def __init__(self, gameState):
        self.gameState = gameState
        self.Sons = []
        colorDict = self.gameState.getColorDict()
        if not self.gameState.isSolved():
            for colorName in colorDict.keys():
                if self.gameState.getPlayerColor != colorDict[colorName]:
                    newState = self.gameState.getStateCopy()
                    newState.changeColor(colorName)
                    self.Sons.append(newState)

    def getTileCount(self):
        return self.gameState.getPlayerCount()

    def getPlayerColor(self):
        return self.gameState.getPlayerColor

    def printNode(self):
        self.gameState.printState()

    def getState(self):
        return self.gameState

    def addSon(self, node):
        self.Sons.append(node)
