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


