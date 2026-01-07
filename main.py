
class StaticList():
    def __init__(self,length):
        self.length = length
        self.list = [None]*length

    def isFull(self):
        if None in self.list:
            return False
        
    def add(self,index,val):
        if not self.isFull():
            self.list[index] = val


