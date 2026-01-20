from staticlist import StaticList

class dynamicList:
    def __init__(self):
        self.list = StaticList(5)

    def display(self):
        for i in range(self.list.length):
            if self.atIndex(i):
                print(self.atIndex(i), end=" ")
        print()

    def append(self,val):
        if self.list.isFull():
            templist = StaticList(self.list.length*2)
            for i in range(self.list.length):
                templist.append(self.atIndex(i))
            
            templist.append(val)
            self.list = templist
        else:
            self.list.append(val)

    def delete(self,index):
        self.list.delete(index)
    
    def pop(self):
        return self.list.pop()

    def atIndex(self,index):
        return self.list.atIndex(index)

    def sum(self):
        sum=0
        for i in range(self.list.length):
            if self.atIndex(i) is not None:
                sum+=self.atIndex(i)
        return sum
    
    def find(self,val):
        for i in range(self.list.length):
            if self.list.atIndex(i)==val:
                return i
        return "Not found"
    
    def extend(self,list):
        for element in list:
            self.append(element)

if __name__=="__main__":
    dl = dynamicList()
    dl.append(0)
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.append(4) #[0, 1, 2, 3, 4]
    dl.append(5) #[0, 1, 2, 3, 4, 5, None, None, None, None]
    print(dl.list.list)
    #dl.delete(0)
    #print(dl.list.list)
    dl.display()
    # print(dl.atIndex(3))
    # print(dl.sum())
    print(dl.pop())
    print(dl.list.list)
    dl.display()
    #print(dl.find(6))

    # dl.extend([6,7,8,9,10])
    # print(dl.list.list)
    # print(dl.sum())
    
