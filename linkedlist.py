class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

#not sure about LinkedList class
class LinkedList:
    def __init__(self,node_val):
        node = Node(node_val)
        self.head = node

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next