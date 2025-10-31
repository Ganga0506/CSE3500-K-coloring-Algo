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
        
        self.E.append({edge1, edge2})

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


    #pop elements, add them back to graph, choose color
    
