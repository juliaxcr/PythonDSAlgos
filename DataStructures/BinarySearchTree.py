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

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            # for identifical value
            if new_node.value == temp.value:
                return False
            # less than
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # greater than
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True                
                temp = temp.right

    def contains(self, value):
#   don't need these two lines:
#        if self.root is None: 
#            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.min_value_node(my_tree.root))

print(my_tree.min_value_node(my_tree.root.right))

print(my_tree.max_value_node(my_tree.root))

print(my_tree.max_value_node(my_tree.root.left))