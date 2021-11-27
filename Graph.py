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
