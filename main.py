status = False
try:
    import snap
    version = snap.Version
    i = snap.TInt(5)
    if i == 5:
        status = True
except:
    pass

if status:
    print("SUCCESS, your version of Snap.py is %s" % (version))
else:
    print("*** ERROR, no working Snap.py was found on your computer")

import snap

def intro():

    # create a graph PNGraph
    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    print("G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges()))

    # create a directed random graph on 100 nodes and 1k edges
    G2 = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    print("G2: Nodes %d, Edges %d" % (G2.GetNodes(), G2.GetEdges()))

    # traverse the nodes
    for NI in G2.Nodes():
        print("node id %d with out-degree %d and in-degree %d" % (
            NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))
    # traverse the edges
    for EI in G2.Edges():
        print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
    print("______________________________________________--")

    # traverse the edges by nodes
    for NI in G2.Nodes():
        for Id in NI.GetOutEdges():
            print("edge (%d %d)" % (NI.GetId(), Id))
    # generate a network using Forest Fire model
    G3 = snap.GenForestFire(1000, 0.35, 0.35)
    print("G3: Nodes %d, Edges %d" % (G3.GetNodes(), G3.GetEdges()))

    # save and load binary
    FOut = snap.TFOut("test.graph")
    G3.Save(FOut)
    FOut.Flush()
    FIn = snap.TFIn("test.graph")
    G4 = snap.TNGraph.Load(FIn)
    print("G4: Nodes %d, Edges %d" % (G4.GetNodes(), G4.GetEdges()))

    # save and load from a text file
    G4.SaveEdgeList("test.txt", "Save as tab-separated list of edges")
    G5 = snap.LoadEdgeList(snap.TNGraph, "test.txt", 0, 1)
    print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

    # generate a network using Forest Fire model
    G6 = snap.GenForestFire(1000, 0.35, 0.35)
    print("G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges()))
    # convert to undirected graph
    G7 = G6.ConvertGraph(snap.TUNGraph)
    print("G7: Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges()))
    # get largest weakly connected component of G
    WccG = G6.GetMxWcc()
    # get a subgraph induced on nodes {0,1,2,3,4,5}
    SubG = G6.GetSubGraph([0,1,2,3,4])
    # get 3-core of G
    Core3 = G6.GetKCore(3)
    # delete nodes of out degree 10 and in degree 5
    G6.DelDegKNodes(10, 5)
    print("G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges()))

    # generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
    G8 = snap.GenPrefAttach(1000, 3)
    print("G8: Nodes %d, Edges %d" % (G8.GetNodes(), G8.GetEdges()))
    # get distribution of connected components (component size, count)
    CntV = G8.GetWccSzCnt()
    # get degree distribution pairs (degree, count)
    CntV = G8.GetOutDegCnt()
    # get first eigenvector of graph adjacency matrix
    EigV = G8.GetLeadEigVec()
    # get diameter of G8
    G8.GetBfsFullDiam(100)
    # count the number of triads in G8, get the clustering coefficient of G8
    G8.GetTriads()
    G8.GetClustCf()

def generate():
    # create a graph TNGraph
    G1 = snap.TNGraph.New()
    G1.AddNode(0)
    G1.AddNode(1)
    G1.AddNode(2)
    G1.AddNode(3)
    G1.AddNode(4)
    G1.AddNode(5)
    G1.AddEdge(0, 1)
    G1.AddEdge(1, 2)
    G1.AddEdge(2, 3)
    G1.AddEdge(3, 4)
    G1.AddEdge(4, 0)
    G1.AddEdge(0, 5)
    G1.AddEdge(5, 4)
    G1.AddEdge(3, 5)
    G1.AddEdge(5, 2)

    print("G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges()))

    for EI in G1.Edges():
        print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))


if __name__ == '__main__':
    generate()
