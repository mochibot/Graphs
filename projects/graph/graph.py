"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print(f'vertex {vertex_id} already exists')
            return
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try: 
            if v2 not in self.vertices:
                raise KeyError
            self.vertices[v1].add(v2)
        except KeyError:
            print(f'Either {v1} or {v2} is not a valid vertex')
            return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        try:
            return self.vertices[vertex_id]
        except KeyError:
            print(f'Vertex {vertex_id} does not exist')
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print('***printing vertex in breadth-first order***')
        queue = Queue()
        visited = {}
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited[vertex] = True
                print(vertex)
                neighbors = self.get_neighbors(vertex)
                if neighbors is not None and len(neighbors) > 0:
                    for neighbor in neighbors:
                        queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print('***printing vertex in depth-first order***')
        stack = Stack()
        visited = {}
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited[vertex] = True
                print(vertex)
                neighbors = self.get_neighbors(vertex)
                if neighbors is not None and len(neighbors) > 0:
                    for neighbor in neighbors:
                        stack.push(neighbor)
        
        

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print('***printing vertex in depth-first order recursively***')
        visited = {}
        def printVisited(v):
            if not v:
                return
            if v not in visited:
                visited[v] = True
                print(v)
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    printVisited(neighbor)
        printVisited(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = {}
        previous = {}   #keep track of previous node coming from 
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex == destination_vertex:
                break
            if vertex not in visited:
                visited[vertex] = True
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)
                    previous[neighbor] = vertex
        #tracing back path from previous
        curr = destination_vertex
        results = []
        while curr in previous:
            results.insert(0, curr)
            curr = previous[curr]
        results.insert(0, curr)
        return results             
                    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = {}
        previous = {}
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex == destination_vertex:
                break
            if vertex not in visited:
                visited[vertex] = True
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)
                    previous[neighbor] = vertex
        curr = destination_vertex
        results = []
        while curr in previous:
            results.insert(0, curr)
            curr = previous[curr]
            if curr == starting_vertex:
                break
        results.insert(0, curr)
        return results  

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = {}
        previous = {}
        def checkVisited(v, d):
            if not v:
                return
            if v == d:
                return
            if v not in visited:
                visited[v] = True
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    previous[neighbor] = v
                    checkVisited(neighbor, d)
        checkVisited(starting_vertex, destination_vertex)
        curr = destination_vertex
        results = []
        while curr in previous:
            results.insert(0, curr)
            curr = previous[curr]
            if curr == starting_vertex:
                break
        results.insert(0, curr)
        return results  


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(5)   #testing adding vertex that already exists
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    graph.add_edge(4, 8)  #testing adding edge to vertex that does not exist
    graph.add_edge(8, 6)  #testing adding edge to vertex that does not exist
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
