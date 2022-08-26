from collections import defaultdict

from algorithm.Node import StateNode


class Graph:
    # Constructor
    def __init__(self, rootNode):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        colorDict = rootNode.gameState.getColorDict()
        for colorName in colorDict.keys():
            if rootNode.gameState.getPlayerColor() != colorDict[colorName]:
                newState = rootNode.gameState.getStateCopy()
                newState.changeColor(colorName)
                self.graph[rootNode].append(StateNode(newState))

    # Function to add an edge to graph
    def addEdge(self, rootNode, sonNode):
        self.graph[rootNode].append(sonNode)

    def generateGraph(self):
        for nodeList in self.graph.values():
            for node in nodeList:
                if not node.gameState.isSolved():
                    colorDict = node.gameState.getColorDict()
                    for colorName in colorDict.keys():
                        if node.gameState.getPlayerColor() != colorDict[colorName]:
                            newState = node.gameState.getStateCopy()
                            newState.changeColor(colorName)
                            self.addEdge(node, StateNode(newState))


    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
        # The function to do DFS traversal. It uses recursive DFSUtil

    def DFS(self):
        # create a set to store all visited vertices
        visited = set()
        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)