from dfs import DepthFirstSearch
from print_graph import print_graph
from print_graph import print_graph_from_dfs
from calculate_positions import calculate_positions
from continous_components import ContinuousComponents
from transpose import transpose


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
    dfs = cc.run()

    print_graph_from_dfs(graph, dfs)


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


# simple_dfs_test()
continuous_components_test()
# transpose_test()
