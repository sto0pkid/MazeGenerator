import random

def generateMaze(options):
    """
    Iterative randomized depth-first search
    """
    width = options['width']
    height = options['height']
    if 'start' in options.keys():
        start = options['start']
    else:
        # top left corner
        start = (0,0)

    if 'end' in options.keys():
        end = options['end']
    else:
        # bottom right corner
        end = (width-1,height-1)

    # random spanning tree
    visited = [[False for _ in range(0,width)] for _ in range(0,height)]
    edges = []
    stack = [((0,0),getNeighbors((0,0),width,height))]
    visited[0][0] = True
    steps = 0
    while len(stack) > 0:
        steps += 1
        cell,neighbors = stack[len(stack)-1]
        if len(neighbors) == 0:
            stack.pop()
            continue
        idx = random.randrange(0,len(neighbors))
        neighbor = neighbors[idx]
        neighbors.pop(idx)
        if not visited[neighbor[1]][neighbor[0]]:
            visited[neighbor[1]][neighbor[0]] = True
            stack.append((neighbor, getNeighbors(neighbor,width,height)))
            edges.append((cell,neighbor))

    return edges

def getNeighbors(cell, width, height):
    neighbors = []
    if(cell[0] > 0):
        neighbors.append((cell[0]-1,cell[1]))
    if(cell[0] < width - 1):
        neighbors.append((cell[0]+1,cell[1]))
    if(cell[1] > 0):
        neighbors.append((cell[0], cell[1]-1))
    if(cell[1] < width - 1):
        neighbors.append((cell[0], cell[1]+1))
    return neighbors




if __name__ == "__main__":
    maze = generateMaze({
        'width': 4,
        'height': 4
    })
    print(maze)
