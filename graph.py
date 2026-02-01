import collections
class Graph:
    def __init__(self):
        self.adj_list = collections.defaultdict(list)

    def add_node(self, node): #O(1)
        if node in self.adj_list:
            print("Node already exists")
            return
        self.adj_list[node]
    
    def add_edge(self,node_1,node_2):#O(1)
        if node_1 not in self.adj_list or node_2 not in self.adj_list:
            print("Both nodes should exist")
            return
        self.adj_list[node_1].append(node_2)
        self.adj_list[node_2].append(node_1)

    def remove_edge(self,node_1,node_2):#O(N)
        if node_1 not in self.adj_list or node_2 not in self.adj_list:
            print("Both nodes should exist")
            return
        if node_2 not in self.adj_list[node_1]:
            print("edge doesnt exist")
            return
        self.adj_list[node_1].remove(node_2)
        self.adj_list[node_2].remove(node_1)  
          
            
    def remove_node(self,node):#(N*M)
        if node not in self.adj_list:
            print("Node doesnt exist")
            return 
        for n in self.adj_list[node]:
            self.adj_list[n].remove(node)
        del self.adj_list[node]

    def has_edge(self,node_1,node_2):#O(N)
        if node_1 not in self.adj_list or node_2 not in self.adj_list:
            return False
        return node_2 in self.adj_list[node_1]
            
    def get_neighbors(self,node):#O(1)
        if node not in self.adj_list:
            return []
        return self.adj_list[node]

    def traverse(self):
        if not self.adj_list:
            print("Graph is empty")
            return
        for node in self.adj_list.keys():
            for nei in self.adj_list[node]:
                print(node,"->",nei,end="\n")
        

    #TODO:  Graph based algos implementation with working examples
if __name__=="__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(1,3)
    # print(graph.adj_list)
    # graph.traverse()
    #graph.remove_edge(1,2)
    # graph.remove_node(1)
    graph.traverse()
    # print(graph.adj_list)
    print(graph.has_edge(1,3))
    print(graph.get_neighbors(4))
