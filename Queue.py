# FIFO - first in, first out
# Dequeue = remove from queue
# Inqueue = add to queue

# Data structures = list
# Remove/add from beginning = O(n)
# Remove/add from end = 0(1)

# Data structure = linked list
# Remove/add from beginning = 0(1)
# Remove from end = 0(n)
# Add from end = O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

