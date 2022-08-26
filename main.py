from game.fillZone import Grid
from algorithm.Node import StateNode
from algorithm.Graph import Graph

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}
numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}

N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)

rootNode = StateNode(fillZone)
graph = Graph(rootNode)
graph.generateGraph()
print('hola')
#while True:
#    color = input('choose a color:\n')
#
#    print('------------------------------')
#    fillZone.changeColor(color)
#    fillZone.printState()
#    if fillZone.isSolved():
#        break
# print('juego terminado')
