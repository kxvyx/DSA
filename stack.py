from dynamiclist import dynamicList

class Stack:
    def __init__(self):
        self.list = dynamicList() 
        self.size = 0

    def display(self):
        for i in range(self.size-1,-1,-1):
            print(self.list.atIndex(i),end=" ")
        print()

    def isEmpty(self):
        return self.size==0

    def push(self,val):
        self.list.append(val)
        self.size+=1

    def pop(self):
        if not self.isEmpty():
            self.size-=1
            return self.list.pop()
        else:
            print("stack is empty")

    def peak(self):
        return self.list.atIndex(self.size-1)

if __name__=="__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.list.list.list)
    # print(stack.size)
    # print("peak :",stack.peak())
    # print("popped :",stack.pop())
    stack.display()
    print("size :",stack.size)
    print("peak :",stack.peak())
    stack.push(5)
    stack.push(6)

    print(stack.list.list.list)
    stack.display()
    print("size :",stack.size)
    print("peak :",stack.peak())
    # print(stack.size)
    # print("peak :",stack.peak())
    