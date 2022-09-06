import time

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def currentMilliTime():
    return round(time.time() * 1000)


def getColors():
    colorDict = {}
    f = open("colors.txt", 'r')
    j = 0
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        colorDict[line] = j
        j += 1
    return colorDict


def printAlgorithmOptions():
    print('Ingrese el algoritmo a utilizar:')
    print('1: dfs')
    print('2: bfs')
    print('3: greedy')
    print('4: A*')


def printHeuristicOptions():
    print('Ingrese que heuristica utilizar:')
    print('0: bronson heuristic')
    print('1: Remaining Colors')
    print('2: most neighbors')
    print('3: Bronson + most neighbors')
    print('4: Bronson + Remaining colors')
    print('5: Remaining colors + most neighbors')

def printPlotOptions():
    print('Desea poder ver el paso a paso del metodo de solucion?')
    print('1: yes')
    print('2: no')


def getTotalExpandedNodes(visited):
    total = 0
    for state in visited:
        total += len(state.getNeighbors())
    return total

def getInvertedColorDict(visited):
    invertedDict = {}
    colorDict = visited[0].getState().getColorDict()
    for key in colorDict.keys():
        invertedDict[colorDict[key]] = key
    return  invertedDict
def getColorSteps(visited):
    numToColor = getInvertedColorDict(visited)
    toReturn = ''
    for node in visited:
        toReturn += numToColor[node.getState().getPlayerColor()]
        if node != visited[len(visited) - 1]:
            toReturn += ' ---> '
    return toReturn

def visualize(visited):
    turns = []
    cmap = ListedColormap(visited[0].getState().getColorDict().keys())
    for node in visited:
        grid = node.getState().getGrid()
        dimension = node.getState().N
        matrix = np.zeros(dimension*dimension, dtype=int)
        matrix = matrix.reshape((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                matrix[i][j] = grid[i][j].tileColor
        turns.append(matrix)
        plt.matshow(matrix, cmap=cmap, vmin=0, vmax=len(visited[0].getState().getColorDict().keys())-1)
        plt.show()




def getBoardDimensions(visited):
    toRet = ''
    toRet += str(visited[0].getState().N)
    toRet += 'x'
    toRet += str(visited[0].getState().N)
    return toRet


def dataSummarize(visited, processingTime, solution, isBfs, plotOption):
    print('board dimension: ', getBoardDimensions(visited))
    print('result: success')
    if isBfs:
        print('solution cost: ', len(solution), ' turns')
    else:
        print('solution cost: ', len(visited), ' turns')
    print('frontier nodes: ', getTotalExpandedNodes(visited), ' nodes')
    print('expanded nodes: ', len(visited), ' nodes')
    print('processing time: ', processingTime, ' ms')
    if isBfs:
        print('solution steps:\n', getColorSteps(solution))
        if plotOption == 1:
            visualize(solution)
    else:
        print('solution steps:\n', getColorSteps(visited))
        if plotOption == 1:
            visualize(visited)
