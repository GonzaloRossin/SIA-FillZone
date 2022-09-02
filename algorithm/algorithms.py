isSolved = False

def dfsIsh(visited,node):
    queue = [node]
    while True:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n.getState().isSolved():
                break
            neighbors = n.getNeighbors()
            queue.append(neighbors[0])


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
