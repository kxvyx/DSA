class UnionFind:
    def __init__(self,length):
        self.rank = [0]*length
        self.parent = [i for i in range(length)]

    def find(self,val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val]) 
        return self.parent[val]
    
    def union(self,val1, val2):
        parent1 = self.find(val1)
        parent2 = self.find(val2)

        if parent1 == parent2:
            return "Already in same set"
        if self.rank[parent1]>self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2]>self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] +=1 

if __name__=="__main__":
    u = UnionFind(5)
    print("parent of 2: ", u.find(2))
    u.union(1,2)
    print("new parent of 2: ", u.find(2))
    u.union(2,3)
    print("parent of 3: ", u.find(3))



