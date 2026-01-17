from staticlist import StaticList

class dynamicList:
    def __init__(self):
        self.list = StaticList(5)

    def append(self,index,val):
        if self.list.isFull():
            templist = StaticList(self.list.length*2)
            for i in range(self.list.length):
                templist.add(i,self.list.list[i])
            
            templist.add(self.list.length,val)
            self.list = templist
        else:
            self.list.add(index,val)

    def delete(self,index):
        self.list.delete(index)
    
    def pop(self):
        last_element = self.list.list[self.list.length-1]
        self.list.delete(self.list.length-1)
        return last_element

    def atIndex(self,index):
        try:
            if index<0 or index>self.list.length:
                raise IndexError("Index is out of range")
            return self.list.list[index]
        except IndexError as e:
            print(e)
        except Exception as e:
            print("something went wrong", e) 

    def sum(self):
        sum=0
        for element in self.list.list:
            if element:
                sum+=element
        return sum
    
    def find(self,val):
        for i in range(self.list.length):
            if self.list.list[i]==val:
                return i
        return "Not found"

if __name__=="__main__":
    dl = dynamicList()
    dl.append(0,0)
    dl.append(1,1)
    dl.append(2,2)
    dl.append(3,3)
    dl.append(4,4) #[0, 1, 2, 3, 4]
    dl.append(5,5) #[0, 1, 2, 3, 4, 5, None, None, None, None]
    dl.delete(4) #[0, 1, 2, 3, None, 5, None, None, None, None]
    dl.append(9,9)
    # print(dl.list.list)
    # print(dl.pop())
    print(dl.list.list)
    print(dl.atIndex(0))
    #print(dl.find(67))

