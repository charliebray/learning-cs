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


    
