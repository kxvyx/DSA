class StaticList:
    #assumed same data type for each element in list
    def __init__(self,length):#O(N)
        self.length = length
        self.list = [None]*length
        self.current = 0

    def isFull(self):#O(1)
        if self.current<self.length:
            return False
        else:
            return True
        
    def add(self,index,val):#O(1)
        try:
            if val is None:
                raise Exception
            if not isinstance(index,int):
                raise Exception
            if not self.isFull() and 0<=index<self.length:
                if self.list[index] is None:
                    self.list[index] = val
                    self.current+=1
                else:
                    self.list[index] = val
        except Exception as e:
            print("None value cannot be added")
        
           
#time complexity make 
    def delete(self,index):#O(1)
        if 0<=index<self.length and self.list[index] is not None:
            self.list[index] = None
            self.current-=1
            


