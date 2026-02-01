class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self):
        pass

    def push(self,val):
        self.heap.append(val)
        self.heapify(self.heap)

    def pop(self):
        pass

    def peek(self):
        return self.heap[0]