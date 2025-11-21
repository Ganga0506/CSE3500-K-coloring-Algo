from general_case_k_coloring import Graph, Node, k_color as k_color_fixed
from k_coloring import Graph as G2, Node as N2, k_color as k_color_auto

# Test Case 1: Simple line graph (chromatic = 2)
def test_line_graph():
    g = G2()
    A, B, C = N2('A'), N2('B'), N2('C')
    for v in [A, B, C]:
        g.add_vertex(v)
    g.add_edge(A, B)
    g.add_edge(B, C)

    chrom = k_color_auto(g)
    assert chrom == 2, f"Expected 2, got {chrom}"

#Test Case 2: Triangle (chromatic = 3)
def test_triangle():
    g = G2()
    A, B, C = N2('A'), N2('B'), N2('C')
    for v in [A, B, C]:
        g.add_vertex(v)
    g.add_edge(A, B)
    g.add_edge(B, C)
    g.add_edge(A, C)

    chrom = k_color_auto(g)
    assert chrom == 3, f"Expected 3, got {chrom}"

#Test Case 3: Square with diagonal (chromatic = 3)
def test_square_with_diagonal():
    g = G2()
    A, B, C, D = N2('A'), N2('B'), N2('C'), N2('D')
    for v in [A, B, C, D]:
        g.add_vertex(v)
    g.add_edge(A, B)
    g.add_edge(B, C)
    g.add_edge(C, D)
    g.add_edge(D, A)
    g.add_edge(A, C) 

    chrom = k_color_auto(g)
    assert chrom == 3, f"Expected 3, got {chrom}"

#Test Case 4: Complete graph K4 (chromatic = 4)
def test_K4():
    g = G2()
    A, B, C, D = N2('A'), N2('B'), N2('C'), N2('D')
    for v in [A, B, C, D]:
        g.add_vertex(v)
    edges = [(A,B),(A,C),(A,D),(B,C),(B,D),(C,D)]
    for e1, e2 in edges:
        g.add_edge(e1,e2)

    chrom = k_color_auto(g)
    assert chrom == 4, f"Expected 4, got {chrom}"

# Test Case 5: Using k=3, triangle should NOT fail
def test_fixed_triangle_valid():
    g = Graph()
    A, B, C = Node('A'), Node('B'), Node('C')
    for v in [A, B, C]:
        g.add_vertex(v)
    g.add_edge(A, B)
    g.add_edge(B, C)
    g.add_edge(A, C)

    # Should color fine with k=3
    g2 = k_color_fixed(g, k=3)
    colors = {v.color for v in g2.V}
    assert len(colors) == 3

# Test Case 6: Using k=2, triangle should FAIL
def test_fixed_triangle_invalid():
    g = Graph()
    A, B, C = Node('A'), Node('B'), Node('C')
    for v in [A, B, C]:
        g.add_vertex(v)
    g.add_edge(A, B)
    g.add_edge(B, C)
    g.add_edge(A, C)


    try:
        k_color_fixed(g, k=2)
        assert False, "Expected AssertionError for non-2-colorable graph"
    except AssertionError:
        pass
