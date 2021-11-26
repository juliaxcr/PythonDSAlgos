# Add and remove from one end
# If you implement using list, use one end for both add and remove
# If you implement using linked list, make sure the end where you remove and add is O(1)
# For LL, beginning of list would be the top of the stack
# head = top, tail = bottom, but bottom is not necessary bc we are only adding/removing from the top

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height is not 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1


my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()