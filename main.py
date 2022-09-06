from Utils import *
from algorithm.Node import StateNode
from algorithm.algorithms import *
from game.fillZone import Grid

colors = getColors()
N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)
rootNode = StateNode(fillZone, None)
printAlgorithmOptions()
algorithmOption = int(input())
if algorithmOption == 1:
    visited = []
    t0 = currentMilliTime()
    dfsIsh(visited, rootNode)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False)
elif algorithmOption == 2:
    visited = []
    queue = []
    t0 = currentMilliTime()
    solution = bfs(visited, rootNode, queue)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, solution, True)
elif algorithmOption == 3:
    printHeuristicOptions()
    option = int(input())
    visited = []
    t0 = currentMilliTime()
    greedy(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False)
elif algorithmOption == 4:
    printHeuristicOptions()
    option = int(input())
    visited = []
    t0 = currentMilliTime()
    aStar(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False)
else:
    print('invalid option')
