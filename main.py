class StaticList:
    #assumed same data type for each element in list
    def __init__(self,length):#O(N)
        self.length = length
        self.list = [None]*length
        self.current_count = 0

    def isFull(self):#O(1)
        if self.current_count<self.length:
            return False
        else:
            return True
        
    def add(self,index,val):#O(1)
        try:
            if val is None:
                raise ValueError("Cannot add None to list")
            if not isinstance(index,int):
                raise TypeError("Index should be integer only")
            if not self.isFull() and 0<=index<self.length:
                if self.list[index] is None:
                    self.current_count+=1
                self.list[index] = val
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception:
            print("Something went wrong :/")
        
    def delete(self,index):#O(1)
        try:
            if not isinstance(index,int):
                raise TypeError("Index should be integer only")
            if 0<=index<self.length and self.list[index] is not None:
                self.list[index] = None
                self.current_count-=1
        except TypeError as e:
            print(e)
        except Exception:
            print("Something went wrong :/")
            


