import networkx as nx
import matplotlib.pyplot as plt

from game.fillZone import Grid
from algorithm.Node import StateNode
from algorithm.Graph import Graph

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}
numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}

N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)

rootNode = StateNode(fillZone)
graph = nx.DiGraph()
nodeQueue = [rootNode]
colorDict = rootNode.getState().getColorDict()
for node in nodeQueue:
    if not node.gameState.isSolved():
        for colorName in colorDict.keys():
            if node.getState().getPlayerColor() != colorDict[colorName]:
                newState = node.getState().getStateCopy()
                newState.changeColor(colorName)
                newNode = StateNode(newState)
                if newNode in graph:
                    graph.add_edge(node, newNode, weight=1)
                else:
                    graph.add_node(newNode)
                    graph.add_edge(node, newNode, weight=1)
                    nodeQueue.append(newNode)

nx.draw(graph)
plt.show()
#for node in graph.nodes:

#while True:
#    color = input('choose a color:\n')
#
#    print('------------------------------')
#    fillZone.changeColor(color)
#    fillZone.printState()
#    if fillZone.isSolved():
#        break
# print('juego terminado')
