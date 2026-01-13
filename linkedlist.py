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
        while current:
            print(current.val)
            current = current.next
    
    def add(self,node): #only add node at end of LL
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    
    def insert(self,position,node): #what if position more than length ?
        if position== 1:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for i in range(position-2):
                cur = cur.next
            next_node = cur.next
            cur.next = node
            node.next = next_node