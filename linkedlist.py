class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.size = 0
        dummy_node = Node(None)
        self.head = dummy_node

    def traverse(self): #O(N)
        current = self.head.next
        while current:
            print(current.val)
            current = current.next

    def get_last_node(self): #O(N)
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur
    
    def insert_at_end(self,node): #O(N)
        last_node = self.get_last_node()
        last_node.next = node
        self.size += 1

    def delete_last_node(self): #O(N)
        if self.size>0:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None
            self.size -= 1

    def insert_at_position(self,position,new_node):#O(N)
        if position < 1 or position > self.size:
            return
        if position== 1:
            next_node = self.head.next
            self.head.next = new_node
            new_node.next = next_node
        else: # 1<position<=self.size:
            cur = self.head
            for i in range(position-1):
                cur = cur.next
            next_node = cur.next 
            cur.next = new_node
            new_node.next = next_node
        self.size+=1
      
    def modify_val_at_position(self,new_val,position):#O(N)
        if position==1:
            self.head.next.val = new_val
        elif position<=self.size:
            cur = self.head
            for i in range(position):
                cur = cur.next
            cur.val = new_val

    def delete_at_position(self,position):
            if position < 1 or position > self.size:
                return
            if position==1:
                next_node = self.head.next.next
                self.head.next = next_node
            else: # 1<position<=self.size:
                cur = self.head
                for i in range(position-1):
                    cur = cur.next
                cur.next = cur.next.next
            self.size-=1
            