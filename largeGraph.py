import random
import sys
import snap

def PrintGStats(s, Graph):
    '''
    Print graph statistics
    '''
    print("graph %s, nodes %d, edges %d, empty %s" % (
        s, Graph.GetNodes(), Graph.GetEdges(),
        "yes" if Graph.Empty() else "no"))

class LargeGraph:
    def __init__(self):
        '''
        Test the default constructor
        '''

        self.Graph = snap.TNEANet.New()
        t = self.Graph.Empty()
        self.PrintGStats("DefaultConstructor:Graph", self.Graph)
        self.FName = "test.graph"

    def PrintGStats(self, s, Graph):
        '''
        Print graph statistics
        '''
        print("graph %s, nodes %d, edges %d, empty %s" % (
            s, Graph.GetNodes(), Graph.GetEdges(),
            "yes" if Graph.Empty() else "no"))

    def AddNode(self, i):
        self.Graph.AddNode(i)
    
    def AddEdge(self, x, y):
        if x != y and not self.Graph.IsEdge(x, y):
            n = self.Graph.AddEdge(x, y)
    
    def GetNumNodes(self):
        # get all the nodes
        NCount = 0
        NI = self.Graph.BegNI()
        while NI < self.Graph.EndNI():
            NCount += 1
            NI.Next()
        return NCount

    def GetNumEdges(self):
        # get all the edges directly
        ECount2 = 0
        EI = self.Graph.BegEI()
        while EI < self.Graph.EndEI():
            ECount2 += 1
            EI.Next()
        return ECount2

    def AddStrAttibute(self, val):
        self.Graph.AddIntAttrN("STR", 0)

    def AddStrData(self, nid, val):
        self.Graph.AddStrAttrDatN(nid, val, "STR")

    def GetAllNodes(self):
        output = []
        attr1 = "STR"
        NI = self.Graph.BegNAStrI(attr1)
        NodeId = 0
        while NI < self.Graph.EndNAStrI(attr1):
            if NI.GetDat() != snap.TStr.GetNullStr():
                print("Node: %i, Val: %s" % (NodeId, NI.GetDat()))
                output.append(NI.GetDat())
                #print("Attribute: %s, Node: %i, Val: %s" % (attr1(), NodeId, NI.GetDat()))
            NodeId += 1
            NI.Next()
        return output
    
    def GetSubGraph(self, nodes):
        self.PrintGStats("SubGraph", self.Graph.GetSubGraph(nodes))

class DGraph:
    def __init__(self) -> None:
        self.Graph = snap.TNGraph.New()

    def PrintGStats(self, s, Graph):
        '''
        Print graph statistics
        '''
        print("graph %s, nodes %d, edges %d, empty %s" % (
            s, Graph.GetNodes(), Graph.GetEdges(),
            "yes" if Graph.Empty() else "no"))

    def AddNode(self, nid):
        self.Graph.AddNode(nid)

    def AddEdge(self, x, y):
        if x != y and not self.Graph.IsEdge(x, y):
            n = self.Graph.AddEdge(x, y)

    def TraverseNodes(self):
        for NI in self.Graph.Nodes():
            print("node id %d with out-degree %d and in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))

    def TraverseEdges(self):
        # traverse the edges
        for EI in self.Graph.Edges():
            print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    def GetSubGraph(self, nodes):
        self.PrintGStats("SubGraph", self.Graph.GetSubGraph(nodes))

if __name__ == '__main__':

    network = LargeGraph()

    for i in range(13):
        network.AddNode(i)

    network.AddStrData(0, "FORT")
    network.AddStrData(1, "FOOT")
    network.AddStrData(2, "FOOD")
    network.AddStrData(3, "FOOL")
    network.AddStrData(4, "GOOD")
    network.AddStrData(5, "POOL")
    network.AddStrData(6, "POLL")
    network.AddStrData(7, "POLE")
    network.AddStrData(8, "PALM")
    network.AddStrData(9, "PALE")
    network.AddStrData(10, "SALE")
    network.AddStrData(11, "SAGE")
    network.AddStrData(12, "SALT")

    network.AddEdge(0, 1)
    network.AddEdge(1, 2)
    network.AddEdge(2, 3)
    network.AddEdge(2, 4)
    network.AddEdge(3, 5)
    network.AddEdge(5, 6)
    network.AddEdge(6, 7)
    network.AddEdge(7, 9)
    network.AddEdge(9, 8)
    network.AddEdge(9, 10)
    network.AddEdge(9, 11)
    network.AddEdge(11, 12)
    # print(network.GetNumNodes)

    dGraph = DGraph()
    for i in range(6):
        dGraph.AddNode(i)
  
    dGraph.AddEdge(0, 1)
    dGraph.AddEdge(1, 2)
    dGraph.AddEdge(2, 3)
    dGraph.AddEdge(3, 4)
    dGraph.AddEdge(4, 0)
    dGraph.AddEdge(0, 5)
    dGraph.AddEdge(5, 4)
    dGraph.AddEdge(3, 5)
    dGraph.AddEdge(5, 2)
    print("----- Sample 1 -----")
    print(sorted(network.GetAllNodes())) #sample 1
    print("----- Extract Subgraph 1 -----")
    network.GetSubGraph([1, 2, 3, 4])
    print("----- Sample 2 -----")
    dGraph.TraverseEdges() #sample 2
    print("----- Extract Subgraph 2 -----")
    dGraph.GetSubGraph([1, 2, 3, 4])
