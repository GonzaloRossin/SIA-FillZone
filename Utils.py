import time
def currentMilliTime():
    return round(time.time() * 1000)


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
