import time


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
    print('1: uncontrolled Tiles')
    print('2: most neighbors')
    print('3: Bronson + most neighbors')
    print('4: Bronson + uncontrolled tiles')
    print('5: uncontrolled tiles + most neighbors')


def getTotalExpandedNodes(visited):
    total = 0
    for state in visited:
        total += len(state.getNeighbors())
    return total


def getColorSteps(visited):
    numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}
    toReturn = ''
    for node in visited:
        toReturn += numToColor[node.getState().getPlayerColor()]
        if node != visited[len(visited) - 1]:
            toReturn += ' ---> '
    return toReturn


def getBoardDimensions(visited):
    toRet = ''
    toRet += str(visited[0].getState().N)
    toRet += 'x'
    toRet += str(visited[0].getState().N)
    return toRet


def dataSummarize(visited, processingTime):
    print('board dimension: ', getBoardDimensions(visited))
    print('result: success')
    print('solution cost: ', len(visited), ' turns')
    print('frontier nodes: ', getTotalExpandedNodes(visited), ' nodes')
    print('expanded nodes: ', len(visited), ' nodes')
    print('processing time: ', processingTime, ' ms')
    print('solution steps:\n', getColorSteps(visited))
