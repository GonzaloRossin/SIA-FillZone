class StateNode:

    def __init__(self, gameState):
        self.gameState = gameState

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.gameState == other.gameState

    def __hash__(self):
        return hash(self.gameState)

    def getTileCount(self):
        return self.gameState.getPlayerCount()

    def getPlayerColor(self):
        return self.gameState.getPlayerColor()

    def printNode(self):
        self.gameState.printState()

    def getState(self):
        return self.gameState
