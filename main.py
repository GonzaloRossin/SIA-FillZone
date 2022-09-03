import networkx as nx
import matplotlib.pyplot as plt

from game.fillZone import Grid
from algorithm.Node import StateNode
from algorithm.Graph import Graph
from algorithm.algorithms import *

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}
numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}
N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)
#fillZone.printState()
rootNode = StateNode(fillZone)
visited = []
queue = []
graph = []
#dfsIsh(visited, rootNode, graph)
aStar(visited, rootNode)
'''while True:
    color = input('choose a color:\n')

    print('------------------------------')
    fillZone.changeColor(color)
    fillZone.printState()
    if fillZone.isSolved():
        break
print('juego terminado')'''
'''visited = []
queue = []
#bfs(visited, rootNode, queue)
dfsIsh(visited,rootNode)'''
for node in visited:
    print('---------------------')
    node.getState().printState()
