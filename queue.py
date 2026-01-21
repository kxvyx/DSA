from doublylinkedlist import DoublyNode, DoublyLinkedList

class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()
        self.size = 0

    def isEmpty(self): #O(1)
        return self.size==0
    
    def display(self): #O(N)
        self.list.traverse()

    def enqueue(self,val):#O(1)
        node = DoublyNode(val)
        self.list.insert_at_end(node)
        self.size+=1

    def dequeue(self):#O(1)
        if not self.isEmpty():
            first_node = self.list.get_val_at_position(1)
            self.list.delete_at_position(1)
            self.size-=1
            return first_node
        else:
            print("Queue is empty")

    def peek(self):#O(1)
        if not self.isEmpty():
            return self.list.get_val_at_position(1)
        else:
            print("Queue is empty")

if __name__=='__main__':
    q = Queue()
    # q.enqueue(11)
    # q.enqueue(12)
    # q.enqueue(13)
    # q.enqueue(14)

    print("is empty:",q.isEmpty())
    print("size: ",q.size)
    print(q.display())

    print("peek is: ",q.peek())

    print(q.dequeue())
    # print("size: ",q.size)
    print(q.display())
    print("peek is: ",q.peek())
    # print(q.peek())