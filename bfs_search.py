class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.distance = 9999
        self.color = 'BLACK'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance) + '  ' + self.vertices[key].color)

    def bfs(self, vert, target):
        q = []
        vert.distance = 0
        vert.color = 'RED'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            if u == target:
                return True
            node_u = self.vertices[u]
            node_u.color = 'RED'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'BLACK':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
        return False

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

mapping = {")": "(", "}": "{", "]": "["}
s = '(())'
for char in s:
    if char in mapping:
        print(char)