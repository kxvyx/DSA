class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def getParentIdx(self,i):
        return (i-1)//2
    
    def hasParent(self,i):
        return self.getParentIdx(i) >=0
    
    def getLeftChildIdx(self,i):
        return 2*i+1
    
    def hasLeftChild(self,i):
        return self.getLeftChildIdx(i) < self.size
    
    def hasRightChild(self,i):
        return self.getRightChildIdx(i) < self.size
    
    def getRightChildIdx(self,i):
        return 2*i+2
    
    def swap(self,idx1 , idx2):
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp

    def heapifyUp(self,idx):
        if ( self.hasParent(idx) and self.heap[self.getParentIdx(idx)] > self.heap[idx]):
            self.swap(self.getParentIdx(idx) , idx)
            idx = self.getParentIdx(idx)
            self.heapifyUp(idx)

    def heapifyDown(self,idx):
        if not self.hasLeftChild(idx):
            return
        smallerChildIndex = self.getLeftChildIdx(idx)
        if self.hasRightChild(idx) and self.heap[self.getRightChildIdx(idx)] < self.heap[smallerChildIndex]:
            smallerChildIndex = self.getRightChildIdx(idx)
        if self.heap[idx] <= self.heap[smallerChildIndex]:
            return
        self.swap(idx,smallerChildIndex)
        self.heapifyDown(smallerChildIndex)


    def push(self,val): 
        self.heap.append(val)
        self.size+=1
        self.heapifyUp(self.size-1)

    def pop(self):
        if self.size == 0:
            print("Heap empty")
            return
        if self.size == 1:
            self.size = 0
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size-=1
        self.heapifyDown(0)
        return min_val


    def peek(self):
        return self.heap[0]
    
if __name__=="__main__":
    heap = MinHeap()
    heap.push(3)
    heap.push(2)
    heap.push(1)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

    print(heap.heap, heap.size)

