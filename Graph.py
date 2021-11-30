# Vertex = node
# Edge = connection
# No limit to how many vertices a vertex can connect to
# Graphs can have weighted edges (e.g. distance, cost, etc.)

# Graphs can be directional or bidirectional
# Facebook connection with friend = bidirectional, goes both ways
# Instagram = directional

# Trees and linked lists are forms of graph

## Adjacency Matrix
# Can represent graph
# Bidirectional matrix is always mirrored, symmetrical
# Weights can be stored as values in the matrix

## Adjacency List
# Can also represent graph

# { 'Node': ['Edge']}

# {
#   'A': ['B', 'E']
#   'B': ['A', 'C']
#   'C': ['B', 'D']
# }

# In matrix, each vertex has to store all vertices, even
# ones not connected to
# Complexity: O(|V|^2)

# In list, it's the number of vertices and edges
# Complexity: O(|V|+|E|)

## Adding new vertex time complexity:
# For matrix: O(|V|^2)      # basically rewriting matrix
# For list: O(1)

## Adding new edge time complexity:
# For matrix: O(1)
# For list: O(1)

## Removing edge between two vetices time complexity:
# For matrix: O(1)
# For list: O(|E|)

## Removing vertex and all its edges time complexity:
# For matrix: O(|V|^2) 
# For list: O(|V|+|E|)

# Bottom line: Adjacency List is most efficient

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            # controls for error if you try to remove edge with vertex that doesn't share any edges
            except ValueError:
                pass
            return True
        return False


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
my_graph.remove_edge(1, 3)

my_graph.print_graph()