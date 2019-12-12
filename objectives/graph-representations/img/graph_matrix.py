class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    
    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            print(f'vertix {vertex_id} already exists')
            return
        self.vertices.append(vertex_id)
        if len(self.edges) == 0:
            self.edges.append([0])
            return
        for i in range(len(self.edges)):
            self.edges[i].append(0)
        self.edges.append([0] * (len(self.edges) + 1))
    
    def add_edge(self, v1, v2):
        try:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.edges[index1][index2] = 1
        except ValueError:
            print(f'either {v1} or {v2} is not a valid vertex') 
            return

    def remove_edge(self, v1, v2):
        try:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.edges[index1][index2] = 0
        except ValueError:
            print(f'either {v1} or {v2} is not a valid vertex') 
            return
    
    def remove_vertex(self, vertex_id):
        try:
            index = self.vertices.index(vertex_id)
            self.vertices.pop(index)
            for i in range(len(self.edges)):
                self.edges[i].pop(index)
            self.edges.pop(index)
        except ValueError:
            print(f'there is no vertex {vertex_id}') 
            return
    
    def find_edge(self, v1, v2):
        try:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            return self.edges[index1][index2] > 0
        except ValueError:
            return f'either {v1} or {v2} is not a valid vertex' 
    
    def find_all_edges(self, vertex_id):
        try: 
            results = []
            index = self.vertices.index(vertex_id)
            for i in range(len(self.edges[index])):
                if self.edges[index][i] > 0:
                    results.append(self.vertices[i])
            return results
        except ValueError:
            return f'there is no vertex {vertex_id}'

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

    print(graph.vertices)
    print(graph.edges)

    graph.remove_edge(2, 3)
    graph.remove_edge(4, 8)
    print(graph.edges)
    graph.remove_vertex(3)
    print(graph.vertices)
    print(graph.edges)
    print(graph.find_edge(1, 3))
    print(graph.find_edge(2, 7))
    print(graph.find_all_edges(2))
    print(graph.find_all_edges(4))
    print(graph.find_all_edges(3))