class Vertex:

    def __init__(self, id):
        self.__id = id
        self.__edgeSet = set()

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getEdgeSet(self):
        return self.__edgeSet

    def addEdge(self,edgeId,debug=False):
        if debug:
            print("Adding edge {} to vertex {}.".format(edgeId,self.__id))
        self.__edgeSet.add(edgeId)

    def removeEdge(self,edgeId,debug=False):
        if debug:
            print("Removing edge {} from vertex {}.".format(edgeId,self.__id))
        self.__edgeSet.remove(edgeId)

    def __str__(self):
        s = ""
        s += "All incident edges of Vertex {} are as follows:\n".format(self.__id)
        for edge in self.__edgeSet:
            s += str(edge) + " "
        s += "\n"
        return s
