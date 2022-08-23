from RubikCube.fillZone import Grid

colors = {'green': 0, 'yellow': 1, 'red': 2, 'blue': 3, 'pink': 4, 'white': 5}
numToColor = {0: 'green', 1: 'yellow', 2: 'red', 3: 'blue', 4: 'pink', 5: 'white'}

N = int(input('Ingrese la dimension del tablero:\n'))
fillZone = Grid(N, colors)
fillZone.printState()

while True:
    color = input('choose a color:\n')
    print('------------------------------')
    fillZone.changeColor(color)
    fillZone.addNeighBors()
    fillZone.printState()
    if fillZone.isSolved():
        break
print('juego terminado')
