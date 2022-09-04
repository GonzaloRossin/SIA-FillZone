import networkx as nx
import matplotlib.pyplot as plt
import time

from game.fillZone import Grid
from algorithm.Node import StateNode
from algorithm.algorithms import *
from Utils import *


colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}
numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}
N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)
rootNode = StateNode(fillZone)
visited = []
queue = []
graph = []
# dfsIsh(visited, rootNode, graph)
t0 = currentMilliTime()
aStar(visited, rootNode)
processing_time = currentMilliTime() - t0
dataSummarize(visited, processing_time)
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
# for node in visited:
#    print('---------------------')
#    node.getState().printState()
