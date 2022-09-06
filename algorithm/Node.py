class StateNode:

    def __init__(self, gameState, father):
        self.gameState = gameState
        self.neighbors = []
        self.father = father

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.gameState == other.gameState

    def __hash__(self):
        return hash(self.gameState)

    def processNeighbors(self):
        if not self.gameState.isSolved():
            colorDict = self.gameState.getColorDict()
            for colorName in colorDict.keys():
                if self.gameState.getPlayerColor() != colorDict[colorName]:
                    newState = self.gameState.getStateCopy()
                    newState.changeColor(colorName)
                    if self.gameState.getPlayerCount() < newState.getPlayerCount():
                        newNode = StateNode(newState, self)
                        self.neighbors.append(newNode)

    def getNeighbors(self):
        if len(self.neighbors) == 0 and not self.gameState.isSolved():
            self.processNeighbors()
        return self.neighbors
    def getParent(self):
        return self.father

    def getTileCount(self):
        return self.gameState.getPlayerCount()

    def getPlayerColor(self):
        return self.gameState.getPlayerColor()

    def printNode(self):
        self.gameState.printState()

    def getState(self):
        return self.gameState

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.gameState.printState()

    def isUseful(self, node):
        return self.gameState.getPlayerCount() < node.gameState.getPlayerCount()
