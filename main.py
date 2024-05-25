from dfs import DepthFirstSearch
from print_graph import print_graph
from print_graph import print_graph_from_dfs
from calculate_positions import calculate_positions
from continous_components import ContinuousComponents
from transpose import transpose
from bfs import bfs


def simple_bfs_test():
    graph = {
        'A': ['B', 'G'],
        'B': ['C', 'D', 'E'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': [],
        'G': ['H'],
        'H': ['I'],
        'I': []
    }

    positions = calculate_positions(graph)

    bfs(graph, 'A', positions)


def simple_dfs_test():
    graph = {
        'A': ['B', 'G'],
        'B': ['C', 'D', 'E'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': [],
        'G': ['H'],
        'H': ['I'],
        'I': []
    }

    dfs = DepthFirstSearch(graph)
    dfs.on_change(lambda: print_graph_from_dfs(graph, dfs))
    dfs.run()

    print("Times: ", dfs.times)
    # Print second value of times tuple ordered by descending
    print("Vertices ordered by descending: ", sorted(dfs.times, key=lambda x: dfs.times[x][1], reverse=True))


def transpose_test():
    graph = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G'],
    }

    positions = calculate_positions(graph)

    transposed = transpose(graph)

    print_graph(graph, positions=positions)
    print_graph(transposed, positions=positions)


def continuous_components_test():
    graph = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G'],
    }

    cc = ContinuousComponents(graph)
    sccs = cc.run()

    print("Edges: ", cc.dfs_transposed.edges)
    print("Strongly Continous Components: ", sccs)

    print_graph_from_dfs(graph, cc.dfs_transposed)


# simple_bfs_test()
# simple_dfs_test()
# transpose_test()
continuous_components_test()
