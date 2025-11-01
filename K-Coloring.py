class Node():
    def __init__(self):
        self.color = 0

    def set_color(self, new_color):
        self.color = new_color

class Graph():
    def __init__(self):
        self.V = {}
        self.E = {}

    def add_vertex(self, new_vert):
        self.V.append(new_vert)

    def add_edge(self, edge1, edge2):
        if(edge1 not in self.V or edge2 not in self.V):
            IndexError("Edge not in graph")
            return -1
        
        self.E.append((edge1, edge2))
        self.E.append((edge2, edge1))

    def get_neighbors(self, origin):
        neighbors = []
        for edge in self.E:
            if(origin == edge[0]):
                neighbors.append(edge[1])
            elif(origin == edge[1]):
                neighbors.append(edge[0])

        return neighbors
                

def heapsort(L):
    """sorts list into a minmum priority heap based off of number of edges (degree)"""

def get_min(L):
    """pops lowest priority, then maintains heap priority"""
    L[0], L[len(L)-1] = L[len(L)-1], L[0]
    min = L.pop()
    downheap(L)

    return min

def downheap(L):
    """Maintains heap property"""

def k_color(graph):
    chromatic_num = 0
    vert_weights = []

    #put all vertex into a list with the degree
    for vert in graph.V:
        num_edges = 0
        for edge in graph.E:
            if(vert in edge):
                num_edges = num_edges +1
        
        vert_weights.append((vert, num_edges))

    #sort the list into a min priority queue
    heapsort(vert_weights)

    #pop elements, add them back to graph, choose color
    while(vert_weights):
        minimum = get_min(vert_weights)
        color = 0
        neighbors = graph.get_neighbors(minimum)
        
