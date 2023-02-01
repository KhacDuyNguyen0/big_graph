"""
A Python program to demonstrate the adjacency
list representation of the graph
"""
 
# A class to represent the adjacency list of the node
 
 
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
 
 
# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
 
    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                print("edge ({} {})".format(i, temp.vertex))
                temp = temp.next
 
# Driver program to the above graph class
if __name__ == "__main__":
    V = 6
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 0)
    graph.add_edge(0, 5)
    graph.add_edge(5, 4)
    graph.add_edge(3, 5)
    graph.add_edge(5, 2)
    graph.print_graph()