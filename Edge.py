class Edge:

    def __init__(self,id, v1=None,v2=None):
        self.__id = id
        self.__v1 = v1
        self.__v2 = v2

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getV1(self):
        return self.__v1

    def setV1(self,v1):
        self.__v1 = v1

    def getV2(self):
        return self.__v2

    def setV2(self,v2):
        self.__v2 = v2

    def __str__(self):
        s = ""
        s += str(self.__id)
        s += "\t\t".format(self.__id)
        s += "{} {}".format(self.__v1,self.__v2)
        s += "\n"
        return s
