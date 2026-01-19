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
        
    def append(self,val):#O(1)
        try:
            if val is None:
                raise ValueError("Cannot add None to list")
            if not self.isFull():
                self.list[self.current_count] = val
                self.current_count+=1
            else:
                print("static list is full")
        except ValueError as e:
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
            
    def pop(self):
        last_element = self.list[self.current_count-1]
        self.delete(self.current_count-1)
        return last_element
    
    def atIndex(self,index):
        try:
            if index<0 or index>self.length:
                raise IndexError("Index is out of range")
            return self.list[index]
        except IndexError as e:
            print(e)
        except Exception as e:
            print("something went wrong", e) 

if __name__=="__main__":
    sl = StaticList(3)
    sl.append(0)
    sl.append(1)
    sl.append(2)
    print(sl.current_count) #3
    print(sl.length) #3
    print(sl.list) #[0, 1, 2]
    print(sl.pop()) #2
    print(sl.list) #[0, 1, None]
    print(sl.atIndex(2)) #None
    # print(sl.list)
    # print(sl.current_count)
    

