import collections
class Graph:
    def __init__(self):
        self.adj_list = collections.defaultdict(list)

    def add_node(self, node): #O(1)
        if node not in self.adj_list:
            self.adj_list[node] = []
        else:
            print("Node already exists")
    
    def add_edge(self,node_1,node_2):#O(N)
        if node_1 and node_2 in self.adj_list:
            self.adj_list[node_1].append(node_2)
            self.adj_list[node_2].append(node_1)
        else:
            print("Both nodes should exist")


    
if __name__=="__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(1,2)
    print(graph.adj_list)
