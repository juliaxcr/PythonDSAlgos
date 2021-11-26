# Nodes have to be laid out in particular way
# Number less than is on left side of node
# Number greater than is on right side of node

## In other words:
# All nodes to the left are less than
# All nodes to the right are greater than


## BST Big O

# First level = 2^1 - 1 = 2
# Second level = 2^2 - 1 = 2^2
# Third level = 2^3 - 1 = 2^3
# Fourth level = 2^4 - 1 = 2^4
# etc ...

# -1 can be dropped because it becomes insigificant

# Each level can represent a step when looking for a node
# All of these steps are O(log n) = divide and conquer

# Best case is perfect tree O(log n)
# Worst case is a single linked list = O(n)

# So, complexity is technically O(n)

# Although, with BST we treat as perfect tree, O(log n)

# lookup(), insert(), and remove() we treat as O(log n), not O(n)

# insert() is (faster) O(1) for linked list
# lookup() and remove() are faster for BST
# if you need DS that can add data quickly and retrival does not matter
# as much, then linked list is better

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # initializes empty BST
    def __init__(self):
        self.root = None

my_tree = BinarySearchTree()
print(my_tree.root)
