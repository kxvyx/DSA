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
            print(current.val,end=" -> ")
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
        else:
            print("list is empty")

    def insert_at_position(self,position,new_node):#O(N)
        try:
            if position < 1 or position > self.size+1:
                raise ValueError("position not in range")

            cur = self.head
            for i in range(position-1):
                cur = cur.next
            next_node = cur.next 
            cur.next = new_node
            new_node.next = next_node
            self.size+=1

        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong:",e)
      
    def modify_val_at_position(self,position,new_val):#O(N)
        try:
            if self.size == 0:
                print("list is empty")
                return
            if position<1 or position>self.size:
                raise ValueError("position not in range")
        
            cur = self.head
            for i in range(position):
                cur = cur.next
            cur.val = new_val

        except ValueError as e:
            print(e)
        except Exception as e:
            print("something went wrong:",e)


    def delete_at_position(self,position):
            try:
                if self.size == 0:
                    print("list is empty")
                    return
                if position<1 or position>self.size:
                    raise ValueError("position not in range")
            
                cur = self.head
                for i in range(position-1):
                    cur = cur.next
                cur.next = cur.next.next
                self.size-=1
            except ValueError as e:
                print(e)  
            except Exception as e:
                print("something went wrong:", e)


if __name__=="__main__":
    LL = LinkedList()
    #print(LL.traverse()) #prints None cz list empty/ dummy node val is None

    LL.insert_at_end(Node(1))
    LL.insert_at_end(Node(2))
    LL.insert_at_end(Node(3))
    LL.insert_at_end(Node(4))
    #print(LL.traverse()) #1->2->3->4->None
    #print(LL.get_last_node().val) #prints 4

    LL.delete_last_node() #removed 4
    LL.insert_at_position(3,Node(2.5)) 
    #print(LL.traverse()) #1->2->2.5->3->None

    LL.delete_at_position(3)
    #print(LL.traverse()) #1->2->3->None

    LL.modify_val_at_position(2,100)
    #print(LL.traverse()) #1->100->3->None

    # for _ in range(LL.size+4): #deleting more times than size
    #     LL.delete_last_node() #o/p list is empty

    LL.insert_at_position(1,Node(6))
    print(LL.traverse()) #6 -> 1 -> 100 -> 3 -> None
    LL.insert_at_position(LL.size+1,Node(6))
    print(LL.traverse()) #6 -> 1 -> 100 -> 3 -> 6 -> None
    LL.insert_at_position(89,Node(4)) #position not in range

    LL.delete_at_position(-9) #position not in range
    LL.delete_at_position(1) 
    print(LL.traverse()) #1 -> 100 -> 3 -> 6 -> None
    LL.delete_at_position(LL.size)
    print(LL.traverse()) #1 -> 100 -> 3 -> None

    LL.modify_val_at_position(1,98)
    print(LL.traverse())