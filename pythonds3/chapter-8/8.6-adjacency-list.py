class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = dict()

    def __repr__(self):
        return f'Vertex({self.key})'

    def __str__(self):
        return f'{self.key} connected to: {self.neighbors.keys()}'

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

class Graph:

    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.set_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(self.vertices[to_vertex], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
    
