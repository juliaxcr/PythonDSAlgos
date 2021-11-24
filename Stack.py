# Add and remove from one end
# If you implement using list, use one end for both add and remove
# If you implement using linked list, make sure the end where you remove and add is O(1)
# For LL, beginning of list would be the top of the stack
# head = top, tail = bottom, but bottom is not necessary

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
