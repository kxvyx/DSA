class DoublyNode:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = DoublyNode(None)
        self.tail = DoublyNode(None)
         
        self.head.next = self.tail
        self.tail.prev = self.head

    def traverse(self):#O(N)
        cur = self.head.next
        while cur!=self.tail:
            print(cur.val,end=" -> ")
            cur = cur.next
    
    def reverseTraverse(self):#O(N)
        cur = self.tail.prev
        while cur!=self.head:
            print(cur.val,end=" -> ")
            cur = cur.prev
    
    def get_last_node_val(self):#O(1)
        return self.tail.prev.val
    
    def get_val_at_position(self,position):#O(N)
        try:
            if position<=0 or position>self.size:
                raise ValueError("position not in range")
            elif position==self.size: 
                return self.get_last_node_val() #O(1)
            else:
                cur = self.head
                for i in range(position):
                    cur = cur.next
                return cur.val
        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong ", e)

    def insert_at_end(self,node):#O(1)
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
        self.size+=1

    def delete_last_node(self):#O(1)
        if self.size>0:
            new_last_node = self.tail.prev.prev
            new_last_node.next = self.tail
            self.tail.prev = new_last_node
            self.size-=1
        else:       
            print("list is empty")

    def insert_at_position(self,position,new_node):
        try:
            if position<=0 or position>self.size+1:
                raise ValueError("position not in range")
            elif position==self.size+1:
                self.insert_at_end(new_node)
            else:
                cur = self.head
                for i in range(position-1):
                    cur = cur.next
                new_node.next = cur.next
                new_node.prev = cur
                cur.next.prev = new_node
                cur.next = new_node
                self.size += 1
        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong", e)

    def delete_at_position(self,position):
        try:
            if position<=0 or position>self.size:
                raise ValueError("position not in range")
            elif position==self.size:
                self.delete_last_node()
            else:
                cur = self.head
                for i in range(position):
                    cur = cur.next
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                self.size -= 1
        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong", e)

    def modify_val_at_position(self,position,new_val):
        try:
            if self.size==0:
                print("list is empty")
                return 
            if position<=0 or position>self.size:
                raise ValueError("position not in range") 
            cur = self.head
            for i in range(position):
                cur = cur.next
            cur.val = new_val
        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong", e)

if __name__=="__main__":
    DLL = DoublyLinkedList()
    DLL.insert_at_end(DoublyNode(1))
    DLL.insert_at_end(DoublyNode(2))
    DLL.insert_at_end(DoublyNode(3))
    # print(DLL.traverse()) #1 -> 2 -> 3 -> None
    # print("size of DLL: ",DLL.size)
    #print(DLL.reverseTraverse())
    # DLL.delete_last_node() #1 -> 2 -> None
    # print(DLL.traverse())
    # print("size of DLL: ",DLL.size)

    DLL.insert_at_position(DLL.size+1,DoublyNode(4))
    print(DLL.traverse())
    #print("size of DLL: ",DLL.size)

    # DLL.delete_at_position(4)
    # print(DLL.traverse())
    # print("last node: ",DLL.get_last_node_val())
    # print("size of DLL: ",DLL.size)

    # DLL.modify_val_at_position(2,20)
    # print(DLL.traverse())

    # print("last node is: ",DLL.get_last_node_val())
    # print("val at position 4: ",DLL.get_val_at_position(4))

