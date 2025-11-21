class Node:
    def __init__(self, name):
        self.color = None
        self.name = name

    def set_color(self, new_color):
        self.color = new_color

class Graph():
    def __init__(self):
        self.V = []
        self.E = []

    def add_vertex(self, new_vert):
        self.V.append(new_vert)

    def add_edge(self, edge1, edge2):
        if edge1 not in self.V or edge2 not in self.V:
            raise IndexError("Edge not in graph")
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

    def remove_vertex(self, vertex):
        # remove vertex and all its edges
        self.V.remove(vertex)
        self.E = [e for e in self.E if vertex not in e]

    def degree(self, vertex):
        return len(self.get_neighbors(vertex))

    def copy(self):
        # copy of graph structure
        new_g = Graph()
        new_g.V = list(self.V)
        new_g.E = list(self.E)
        return new_g


def k_color(graph, k):
    stack = []
    temp_graph = graph.copy()

    #Simplification (remove vertices)
    while temp_graph.V: #while we stil have vertices to chase
        low_deg_vertex = None  #set min vertex and degree to none
        min_degree = float('inf')

        for v in temp_graph.V:     #go through remaining vertices in insertion order
            d = temp_graph.degree(v)  
            if d < k:              #if vertex is less than k(# colors)
                low_deg_vertex = v #set lowest vertex to it and remove it and stack it right away
                break
            elif d < min_degree:  #if we cannot find one less than k, choose the lowest and remove it anyway
                low_deg_vertex = v
                min_degree = d
      #push the vertex with the lowest degree/degree < k onto the stack
      #remove it and its edges from the graph
      #do the same process until there are no vertices to put onto the stack
        stack.append(low_deg_vertex)
        temp_graph.remove_vertex(low_deg_vertex)

    #Coloring (reinsert vertices)
    while stack:
        v = stack.pop() #remove the last item in the stack
        used_colors = set()  #all colors used

        for neighbor in graph.get_neighbors(v): #takes all nieghboring colors, if a color is used in a neighbor adds it to the used set
            if neighbor.color is not None: 
                used_colors.add(neighbor.color)

        # Assign lowest available color
        for color in range(k):                 #colors are from 0 to k-1 in this case
            if color not in used_colors:
                v.set_color(color)              #makes color lowest color not used by the neighbors
                break
        else:
            # If all colors are used, assign a new color (graph IS NOT k-colorable in this case)
            v.set_color(len(used_colors))  #should we make this an error?

    return graph


G = Graph()
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

for node in [A, B, C, D, E]:
    G.add_vertex(node)

edges = [(A, B), (A, C), (B, C), (C, D), (D, E)]
for n1, n2 in edges:
    G.add_edge(n1, n2)

# Run graph coloring
k_color(G, k=3)

# Print results
print("Final coloring:")
for v in G.V:
    print(f"{v.name}: color {v.color}")

#gets the same answer that I got on paper, I believe this is correct(may need to improve effieiency however)!

