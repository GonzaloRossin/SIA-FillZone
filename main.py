from Utils import *
from algorithm.Node import StateNode
from algorithm.algorithms import *
from game.fillZone import Grid

colors = getColors()
N = int(input('Ingrese la dimension del tablero:\n'))
if N < 1:
    print('Invalid size dimensions, try again')
    exit(1)
fillZone = Grid(N, colors)
rootNode = StateNode(fillZone, None)
printAlgorithmOptions()
algorithmOption = int(input())
if algorithmOption == 1:
    visited = []
    printPlotOptions()
    plotOption = int(input())
    if plotOption < 1 or plotOption > 2:
        print('choose a valid option to advance, try again')
        exit(3)
    t0 = currentMilliTime()
    dfsIsh(visited, rootNode)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False, plotOption)
elif algorithmOption == 2:
    visited = []
    queue = []
    printPlotOptions()
    plotOption = int(input())
    if plotOption < 1 or plotOption > 2:
        print('choose a valid option to advance, try again')
        exit(1)
    t0 = currentMilliTime()
    solution = bfs(visited, rootNode, queue)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, solution, True, plotOption)
elif algorithmOption == 3:
    printHeuristicOptions()
    option = int(input())
    if option < 0 or option > 5:
        print('choose a valid option to advance, try again')
        exit(4)
    visited = []
    printPlotOptions()
    plotOption = int(input())
    if plotOption < 1 or plotOption > 2:
        print('choose a valid option to advance, try again')
        exit(3)
    t0 = currentMilliTime()
    greedy(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False, plotOption)
elif algorithmOption == 4:
    printHeuristicOptions()
    option = int(input())
    if option < 0 or option > 5:
        print('choose a valid option to advance, try again')
        exit(4)
    visited = []
    printPlotOptions()
    plotOption = int(input())
    if plotOption < 1 or plotOption > 2:
        print('choose a valid option to advance, try again')
        exit(3)
    t0 = currentMilliTime()
    aStar(visited, rootNode, option)
    processing_time = currentMilliTime() - t0
    dataSummarize(visited, processing_time, None, False, plotOption)
else:
    print('invalid option')
