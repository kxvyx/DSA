import collections
class Graph:
    def __init__(self):
        self.adj_list = collections.defaultdict(list)

    def add_node(self, node): #O(1)
        if node not in self.adj_list:
            self.adj_list[node]
        else:
            print("Node already exists")
    
    def add_edge(self,node_1,node_2):#O(1)
        if node_1 in self.adj_list and node_2 in self.adj_list:
            self.adj_list[node_1].append(node_2)
            self.adj_list[node_2].append(node_1)
        else:
            print("Both nodes should exist")
    
    def remove_edge(self,node_1,node_2):#O(N)
        if node_1 in self.adj_list and node_2 in self.adj_list:
            if node_2 in self.adj_list[node_1]:
                self.adj_list[node_1].remove(node_2)
                self.adj_list[node_2].remove(node_1)
           
        else:
            print("Both nodes should exist")

    def remove_node(self,node):#(N*M)
        if node in self.adj_list:
            for n in self.adj_list[node]:
                self.adj_list[n].remove(node)
            del self.adj_list[node]
        else:
            print("Node doesnt exist")

    def has_edge(self,node_1,node_2):#O(N)
        if node_1 in self.adj_list and node_2 in self.adj_list:
            return node_2 in self.adj_list[node_1]
        else:
            return False
        
    def get_neighbors(self,node):#O(1)
        if node in self.adj_list:
            return self.adj_list[node]
        else:
            return []
    
    def traverse(self):
        if self.adj_list:
            for node in self.adj_list.keys():
                for nei in self.adj_list[node]:
                    print(node,"->",nei,end="\n")
        else:
            print("Graph is empty")
        

    #TODO:  Graph based algos implementation with working examples
if __name__=="__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(1,3)
    print(graph.adj_list)
    graph.traverse()
    # graph.remove_edge(1,2)
    # graph.remove_node(1)
    # print(graph.adj_list)
    # print(graph.has_edge(1,3))
    # print(graph.get_neighbors(4))
