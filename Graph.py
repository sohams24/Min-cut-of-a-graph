from Edge import Edge
from Vertex import Vertex
import random

class Graph:

    def __init__(self,filename,debug = False):
        self.__vertexDict = dict()
        self.__edgeDict = dict()
        self.__no_of_vertices = 0
        self.__no_of_edges = 0

        if debug:
            print("Parsing Graph from File:{}".format(filename))

        with open(filename,'r') as f:
            for line in f:
                line = line.strip()
                line_arr = line.split('\t')
                root_vertex_id = line_arr[0]
                if root_vertex_id not in self.__vertexDict:
                    self.__vertexDict[root_vertex_id] = Vertex(root_vertex_id)
                    self.__no_of_vertices += 1
                for vertex_id in line_arr[1:]:
                    new_edge_id = str(root_vertex_id)+"&"+str(vertex_id)
                    if vertex_id not in self.__vertexDict:
                        self.__vertexDict[vertex_id] = Vertex(vertex_id)
                        self.__no_of_vertices += 1
                    if not(new_edge_id in self.__edgeDict or str(vertex_id)+"&"+str(root_vertex_id) in self.__edgeDict):
                        new_edge = Edge(new_edge_id,root_vertex_id,vertex_id)
                        self.__edgeDict[new_edge_id] = new_edge
                        self.__no_of_edges += 1
                        self.__vertexDict[vertex_id].addEdge(new_edge_id,debug)
                        self.__vertexDict[root_vertex_id].addEdge(new_edge_id,debug)


    def getEdgeDict(self):
        return self.__edgeDict

    def getVertexDict(self):
        return self.__vertexDict

    def getVertexCount(self):
        return self.__no_of_vertices

    def getEdgeCount(self):
        return self.__no_of_edges

    def __str__(self):
        s = "Edges are as follows\n"
        for edgeId in self.__edgeDict:
            s += self.__edgeDict[edgeId].__str__()
        s += "\n"
        s += "Vertices are as follows\n"
        for vertex_id in self.__vertexDict:
            s += self.__vertexDict[vertex_id].__str__()
            s += "\n"
        return s


    def karger(self,debug=False):
        while len(self.__vertexDict) > 2:
            selected_edge_id = random.choice(list(self.__edgeDict.keys()))
            selected_edge = self.__edgeDict[selected_edge_id]
            absorbing_vertex_id = selected_edge.getV1()
            vertex_to_be_absorbed_id = selected_edge.getV2()
            if debug:
                print("The edge to be contracted is {}".format(selected_edge_id))
                print("The vertex to be kept is {}".format(absorbing_vertex_id))
                print("The vertex to be absorbed is {}".format(vertex_to_be_absorbed_id))

            absorbing_vertex = self.__vertexDict[absorbing_vertex_id]
            vertex_to_be_absorbed = self.__vertexDict[vertex_to_be_absorbed_id]

            vertex_to_be_absorbed.removeEdge(selected_edge_id,debug)
            absorbing_vertex.removeEdge(selected_edge_id,debug)

            for edgeId in vertex_to_be_absorbed.getEdgeSet().copy():
                edge = self.__edgeDict[edgeId]
                if edge.getV1() == vertex_to_be_absorbed_id:

                    if debug:
                        print("Changing v1 of edge {} from {} to {}".format(edgeId,edge.getV1(),absorbing_vertex_id))
                    edge.setV1(absorbing_vertex_id)

                if edge.getV2() == vertex_to_be_absorbed_id:

                    if debug:
                        print("Changing v2 of edge {} from {} to {}".format(edgeId,edge.getV2(),absorbing_vertex_id))
                    edge.setV2(absorbing_vertex_id)


                if edgeId in absorbing_vertex.getEdgeSet():
                    absorbing_vertex.removeEdge(edgeId,debug)
                    vertex_to_be_absorbed.removeEdge(edgeId,debug)
                    del self.__edgeDict[edgeId]
                    if debug:
                        print("Deleted self loop {}".format(edgeId))
                else:
                    absorbing_vertex.addEdge(edgeId,debug)


            del self.__vertexDict[vertex_to_be_absorbed_id]
            if debug:
                print("Deleted vertex {} permanantly".format(vertex_to_be_absorbed_id))
            del self.__edgeDict[selected_edge_id]
            if debug:
                print("Deleted edge {} permanantly".format(selected_edge_id))
