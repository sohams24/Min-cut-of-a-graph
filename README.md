# Stanford-Algorithms-Part-1---Assignment-3
In this project we implement Karger's randomized contraction algorithm to find the min-cut of a given input graph.
The graph is provided in a text file named "kargerMinCut.txt" in adjecency list representation. Every line represents a vertex followed by all the vertices adjecent to it separated with tabs.
A test file of a small graph is also provided in "test.txt".
An output file named "minCutOutput.txt" is generated that has the list of the edges in the min-cut represented with the two end vertices.

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Add your input text file to the folder (the graph in your input file should have the format same as the one in "kargerMinCut.txt")
3)  Specify the name of your input file in the file "kargerMinCut.py" on line 5.
4)  Set the number of iterations you wish to run in file "kargerMinCut.py" on line 11.
5)  If you wish to print the debug messages, set the value of 'debug' to 'True' on line 6 in file "kargerMinCut.py" 
6)  Run the file "kargerMinCut.py".
7)  Check the file "minCutOutput.txt" for the output.

Vertex.py:
This file defines the "Vertex" class.
Every vertex has an "id" and a set "edgeSet" that stores all the "ids" of all the edges incident to that vertex.

Edge.py:
This file defines the "Edge" class.
Every edge has an "id" and two end vertices named "v1" and "v2".

Graph.py:
This file defines the "Graph" class.
The graph has two dictonaries named "vertexDict" and "edgeDict".
"vertexDict" stores all the "Vertex" instances with their respective "ids" as keys.
"edgeDict" stores all the "Edge" instances with their respective "ids" as keys.
The method "karger" computes the min-cut.

kargerMinCut.py:
This is the file that creates the "Graph" instance by passing the input file.
Here we call the "karger" method from the graph instance.
Since the Karger's algorithm is a randomized algorithm, it does not gurrantee to give the correct result in a single iteration.
Thus we run multiple iterations of the algorithm and choose the result that gives minimum number of edges in the min-cut.
