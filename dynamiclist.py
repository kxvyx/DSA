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

if __name__=="__main__":
    dl = dynamicList()
    dl.append(0,0)
    dl.append(1,1)
    dl.append(2,2)
    dl.append(3,3)
    dl.append(4,4) #[0, 1, 2, 3, 4]
    dl.append(5,5) #[0, 1, 2, 3, 4, 5, None, None, None, None]
    dl.delete(4) #[0, 1, 2, 3, None, 5, None, None, None, None]

    print(dl.list.list)


