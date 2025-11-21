from k_coloring import Node as N1, Graph as G1, k_color as K1
from general_case_k_coloring import Node as N2, Graph as G2, k_color as K2

def sudoku_graph(Node, Graph):

    g = Graph()
    sudoku_nodes = {}

    for row in range(9):
        for column in range(9):
            index = row*9 + column
            node = Node(name=index)
            sudoku_nodes[(row, column)] = node
            g.add_vertex(node)
    
    for row_1 in range(9):
        for column_1 in range(9):
            for row_2 in range(9):
                for column_2 in range(9):
                    if (row_1, column_1) == (row_2, column_2):
                        continue

                    same_row = (row_1 == row_2) # Should be False since they're supposed to be different
                    same_column = (column_1 == column_2) # Samesies, False cos they should be different
                    same_box = (row_1 // 3 == row_2 // 3) and (column_1 // 3 == column_2 // 3)
    
                    if same_row or same_column or same_box:
                        g.add_edge(sudoku_nodes[(row_1, column_1)], sudoku_nodes[(row_2, column_2)])
    
    return g, sudoku_nodes

def make_board(board, nodes):
    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value != 0:
                nodes[(row, column)].set_color(value - 1)
            else:
                nodes[(row, column)].set_color(None)

def extract_board(Nodes):
    board = [[0] * 9 for i in range(9)]

    for (row, column), node in Nodes.items():
        if node.color is None:
            board[row][column] = 0
        else:
            board[row][column] = node.color + 1
    
    return board

def solve_using_k_coloring(Graph, nodes):
    K1(Graph, 9)
    
    return extract_board(nodes)

def solve_using_general_case_k_coloring(Graph, nodes):
    chromatic_number = K2(Graph)
    board = extract_board(nodes)

    return chromatic_number, board

def print_sudoku_board(board):
    for row_1 in range(9):
        if row_1 % 3 == 0 and row_1 != 0:
            print("-" * 25)
        
        row_2 = ""
        for column in range(9):
            if column % 3 == 0 and column != 0:
                row_2 += " |"
            row_2 += f" {board[row_1][column]}"
        
        print(row_2)

if __name__ == '__main__':
    
    # Test board to make sure code works as intended
    # Asked 

    sample_board = [
        [0,6,0, 0,0,0, 8,0,0],
        [0,0,0, 0,7,3, 0,9,0],
        [3,0,9, 0,0,0, 0,0,1],

        [0,0,0, 3,0,0, 0,0,7],
        [0,0,2, 0,0,0, 9,0,0],
        [7,0,0, 0,0,2, 0,0,0],

        [9,0,0, 0,0,0, 3,0,4],
        [0,4,0, 2,8,0, 0,0,0],
        [0,0,3, 0,0,0, 0,7,0],
    ]

    Graph1, Node1 = sudoku_graph(N1, G1)
    make_board(sample_board, Node1)
    print("Using k_coloring:")
    k_coloring_board = solve_using_k_coloring(Graph1, Node1)
    print_sudoku_board(k_coloring_board)

    Graph2, Node2 = sudoku_graph(N2, G2)
    make_board(sample_board, Node2)


    print()
    print()
    print()

    print("Using general_case_k_coloring_solution:")
    chromatic_number, general_case_k_coloring_board = solve_using_general_case_k_coloring(Graph2, Node2)
    print(f"Chromatic Number = {chromatic_number}")
    print_sudoku_board(general_case_k_coloring_board)
