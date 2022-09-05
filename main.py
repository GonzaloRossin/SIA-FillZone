from Utils import *
from algorithm.Node import StateNode
from algorithm.algorithms import *
from game.fillZone import Grid

colors = getColors()
N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)
rootNode = StateNode(fillZone)
printAlgorithmOptions()
algorithmOption = int(input())
if algorithmOption == 1:
    visited = []
    t0 = currentMilliTime()
    dfsIsh(visited, rootNode)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time)
elif algorithmOption == 2:
    visited = []
    queue = []
    t0 = currentMilliTime()
    bfs(visited, rootNode, queue)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time)
elif algorithmOption == 3:
    printHeuristicOptions()
    option = input()
    visited = []
    t0 = currentMilliTime()
    greedy(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time)
elif algorithmOption == 4:
    printHeuristicOptions()
    option = int(input())
    visited = []
    t0 = currentMilliTime()
    aStar(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time)
else:
    print('invalid option')

