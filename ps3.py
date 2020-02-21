import random

class MyGraph:
    ''' Class MyGraph Contains the Graph '''

    def __init__(self, filename='kargerMinCut.txt', debug=False, test=False):
        self.vertices = {}
        if debug:
            print('Parsing Graph from File:%s'%(filename))
        fo = open(filename, 'r')
        for line in fo:
            line = line.strip()
            line_arr = line.split('\t')
            line_arr = [int(x, 10) for x in line_arr]
            root_vertex = line_arr[0]
            self.vertices[root_vertex] = line_arr[1:]
        fo.close()
        self.vertex_count=len(self.vertices)

    def __str__(self):
        str1 = '*'*30 + '\n'
        str1 += format('Total Number of vertices:%d\n\n'%(len(self.vertices)))
        str1 += '\nDisplaying the vertices Dict:\n\n'
        for root_vertex, connect_array in self.vertices.items():
            str1 += format('Vertex:%d connects%s\n\n'%(root_vertex, connect_array))
        str1 += '*'*30 + '\n'
        return str1

    def __rand_sel_merge_vertex(self, debug=False):
        ''' Function to Randomly Select a merge Vertex '''
        temp_list = list(self.vertices.keys())
        if debug:
            print("current vertices keys:%s"%(temp_list))
        merge_vertex = random.choice(temp_list)
        if debug:
            print('Randomly Selected merge Vertex:', merge_vertex)
        return merge_vertex

    def __rand_sel_delete_vertex(self, merge_vertex, debug=False):
        ''' Function to Randomly Select a delete Vertex '''
        if debug:
            print('Randomly selecting delete Vertex for merge Vertex:', merge_vertex)
        delete_vertex = random.choice(self.vertices[merge_vertex])
        self.vertices[merge_vertex] = [x for x in self.vertices[merge_vertex] if x != delete_vertex]
        if debug:
            print('Randomly selected delete Vertex :', delete_vertex)

        return delete_vertex

    def __delete_delArray_mergeEntry(self, merge_vertex, delete_vertex, debug=False):
        ''' Function to Delete the merge Vertex entry from the array of delete Vertex '''
        if debug:
            print("Removing %d Vertex from %s"%(merge_vertex, self.vertices[delete_vertex]))
        self.vertices[delete_vertex] = [x for x in self.vertices[delete_vertex] if x != merge_vertex]

    def __merge_delArray_delete_delArray(self, merge_vertex, delete_vertex, debug=False):
        ''' Function to extend the merge array with the delete array and then delete the delete array '''
        self.vertices[merge_vertex].extend(self.vertices[delete_vertex])
        for Vertex in self.vertices[delete_vertex]:
            for index, value in enumerate(self.vertices[Vertex]):
                if value == delete_vertex:
                    self.vertices[Vertex][index] = merge_vertex
        self.vertices.pop(delete_vertex)
        if debug:
            print("Extended the merge array of Vertex %d with the delete array %d and then deleted the delete array %d"%(merge_vertex, delete_vertex, delete_vertex))

    def find_min_cut(self, debug=False):
        while len(self.vertices) > 2:
            merge_vertex = self.__rand_sel_merge_vertex(debug)
            delete_vertex = self.__rand_sel_delete_vertex(merge_vertex, debug)
            self.__delete_delArray_mergeEntry(merge_vertex, delete_vertex, debug)
            self.__merge_delArray_delete_delArray(merge_vertex, delete_vertex, debug)
            if debug:
                print(self.__str__())
        temp_list = list(self.vertices.keys())
        key_0 = temp_list[0]
#         print("Min Cut:%d"%(len(self.vertices[key_0])))
        return len(self.vertices[key_0])

debug = False
g1 = MyGraph('kargerMinCut.txt', test=False, debug=debug)
# print(g1)
repeatitions = len(g1.vertices)**2
min_cut = repeatitions
for i in range(0, 100):
    g1 = MyGraph('kargerMinCut.txt', test=False, debug=debug)
    if(debug):
        print(g1)
    current_min_cut = g1.find_min_cut(debug)
    if current_min_cut < min_cut:
        min_cut = current_min_cut
print("Minimum cut: ",min_cut)

