

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.discovery = 0
        self.finish = 0
        self.color = 'BLACK'

    def add_neighbor(self, v):
        if v not in set(self.neighbors):
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}
    time = 0

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
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].discovery) + " / " + str(self.vertices[key].finish) + '  ' + self.vertices[key].color)

    def _dfs_util(self, vertex):
        global time
        vertex.color = 'GREEN'
        vertex.discovery = time
        time += 1

        for v in vertex.neighbors:
            if self.vertices[v].color == 'BLACK':
                self._dfs_util(self.vertices[v])

        vertex.color = 'RED'
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs_util(vertex)




g = Graph()
a = Vertex('A')
g.add_vertex(a)
# g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()


print('DFS with Tree')

class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.value = n


def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

def searchPreorder(root, node):
    if root:
        print(root.value)
        searchPreorder(root.left, node)
        searchPreorder(root.right, node)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.right.left.right = Node(9)

printPreorder(root)