from Graph import Graph
import copy
import os

filename = "kargerMinCut.txt"
debug = False
g = Graph(filename,debug)
minCutlen = len(g.getEdgeDict())
n = g.getVertexCount()
m = g.getEdgeCount()
iterations = 1000
for i in range(1,iterations+1):
    g_copy = copy.deepcopy(g)
    g_copy.karger(debug)
    new_minCutlen = len(g_copy.getEdgeDict())
    if new_minCutlen < minCutlen:
        minCutlen = new_minCutlen
        minCut = g_copy.getEdgeDict()
    if i%100 == 0:
        print("{} iterations completed. Remaining:{}".format(i,iterations-i))
print("Number of edges in the min-cut:",minCutlen)
print('Check the file "minCutOutput" for the min-cut edges.')
cwd = os.getcwd()
f = open(cwd+"\minCutOutput.txt",'w')
f.write("Following are the edges in the min-cut of the Graph {}\n".format(filename))
for edgeId in minCut:
    f.write("{} - {}\n".format(g.getEdgeDict()[edgeId].getV1(),g.getEdgeDict()[edgeId].getV2()))
f.write("Number of edges in the min-cut:{}".format(minCutlen))
f.close()


