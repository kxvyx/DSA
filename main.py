class StaticList():
    def __init__(self,length):
        self.length = length
        self.list = [None]*length

    def isFull(self):
        if None in self.list:
            return False
        
    def add(self,index,val):
        if not self.isFull() and index<self.length:
            self.list[index] = val

    def delete(self,index):
        if index<self.length:
            self.list[index] = None
            


