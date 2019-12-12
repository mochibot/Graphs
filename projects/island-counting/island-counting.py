'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

Example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

from util import Queue


def get_neighbors(vertex, graph):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    #check north
    if y > 0 and graph[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    #check south
    if y < len(graph) - 1 and graph[y + 1][x]:
        neighbors.append((x, y + 1))
    #check west
    if x > 0 and graph[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    #check east
    if x < len(graph[0]) - 1 and graph[y][x + 1]:
        neighbors.append((x + 1, y))
    return neighbors
    

def bft(x, y, matrix, visited):
    q = Queue()
    q.enqueue((x, y))
    while q.size() > 0:
        node = q.dequeue()
        x = node[0]
        y = node[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):
    '''
    Loop through the matrix, do BFT and count how many times the BFT occurs
    Create a visited matrix of same dimensions as islands, initialize all values to False
    Create a counter, initialize to 0
    Loop through each node in the islands matrix
        If node has not been visited
            If node is 1
                Do BFT and mark node as visited
                Increment counter by 1
    Return counter
    '''
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j]:
                if matrix[i][j] == 1:
                    visited = bft(j, i, matrix, visited)
                    counter += 1
    return counter

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands)) #returns 4

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))   #returns 14