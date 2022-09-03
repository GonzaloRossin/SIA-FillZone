from game.tile import tile
import networkx as nx

isSolved = False


def dfsIsh(visited, node):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getState().isSolved():
                break
            neighbors = n.getNeighbors()
            queue.append(neighbors[0])  # all neighbors can reach solution so I can choose any neighbor I want


def aStar(visited, node):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getState().isSolved():
                break
            neighborPicked = neighBorPicker(n.getNeighbors())
            queue.append(neighborPicked)

def bronsonHeuristic(neighbor):
    DISTANCE = 0
    state = neighbor.getState()
    playerTile = tile(state.N + 1, state.N + 1, 0,
                      True)  # this tile does not exist in grid and represents all player tiles in graph
    graph = generateBronsonGraph(neighbor.getState(), playerTile)
    len_path = dict(nx.all_pairs_dijkstra(graph))
    maxValue = 0
    for key in len_path[playerTile][DISTANCE]:
        if len_path[playerTile][DISTANCE][key] > maxValue:
            maxValue = len_path[playerTile][DISTANCE][key]
    return maxValue

def neighBorPicker(neighbors):
    neighborValues = []
    EDGE_WEIGHT =1
    for neighbor in neighbors:
        neighborValue = bronsonHeuristic(neighbor)
        neighborValues.append(neighborValue)

    minValue = neighborValues[0]+EDGE_WEIGHT #get MinValue neighbor
    index = 0
    for i in range(len(neighborValues)-1):
        if neighborValues[i+1]+EDGE_WEIGHT < minValue:
            index = i+1
            minValue = neighborValues[i+1]+EDGE_WEIGHT

    return neighbors[index]


def bfs(visited, node, queue):  # function for BFS
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        visited.append(m)
        if m.getState().isSolved():
            print('solved')
            break
        else:
            neighbors = m.getNeighbors()
            for node in neighbors:
                if m.isUseful(node) and node not in visited:
                    queue.append(node)

    queue.clear()


def getUncontrolledColors(state):
    colorValues = state.getColorDict().values()
    colorSeen = []
    for Tile in state.nonControlled:
        if len(colorSeen) == len(colorValues):
            break
        if Tile.tileColor not in colorSeen:
            colorSeen.append(Tile.tileColor)

    return len(colorSeen)


def generateBronsonGraph(state, playerTile):
    grid = state.getGrid()
    graph = nx.Graph()
    graph.add_node(playerTile)
    for i in range(state.N):
        for j in range(state.N):
            Tile = grid[i][j]
            if not Tile.getIsPlayer():
                graph.add_node(Tile)
                if Tile.hasTop():
                    top = grid[Tile.x - 1][Tile.y]
                    graph.add_node(top)
                    if top.getIsPlayer():
                        graph.add_edge(playerTile, Tile, weight=1)
                    elif Tile.hasSameColor(top):
                        graph.add_edge(Tile, top, weight=0)
                    else:
                        graph.add_edge(Tile, top, weight=1)

                if Tile.hasLeft():
                    left = grid[Tile.x][Tile.y - 1]
                    graph.add_node(left)
                    if left.getIsPlayer():
                        graph.add_edge(playerTile, Tile, weight=1)
                    elif Tile.hasSameColor(left):
                        graph.add_edge(Tile, left, weight=0)
                    else:
                        graph.add_edge(Tile, left, weight=1)

                if Tile.hasRight(state.N):
                    right = grid[Tile.x][Tile.y + 1]
                    graph.add_node(right)
                    if right.getIsPlayer():
                        graph.add_edge(playerTile, Tile, weight=1)
                    elif Tile.hasSameColor(right):
                        graph.add_edge(Tile, right, weight=0)
                    else:
                        graph.add_edge(Tile, right, weight=1)

                if Tile.hasDown(state.N):
                    down = grid[Tile.x + 1][Tile.y]
                    graph.add_node(down)
                    if down.getIsPlayer():
                        graph.add_edge(playerTile, Tile, weight=1)
                    elif Tile.hasSameColor(down):
                        graph.add_edge(Tile, down, weight=0)
                    else:
                        graph.add_edge(Tile, down, weight=1)
    return graph


def BronsonDistance(state):
    graph = generateBronsonGraph(state)
    len_path = dict(nx.all_pairs_dijkstra(graph))
