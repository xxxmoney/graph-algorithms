from dfs import DepthFirstSearch
from dfs import VertexState
from print_graph import print_graph
from calculate_positions import calculate_positions
from continous_components import ContinuousComponents


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

    positions = calculate_positions(graph)

    dfs = DepthFirstSearch(graph)

    dfs.on_change(
        lambda: print_graph(
            graph,
            grey_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITING],
            black_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITED],
            positions=positions)
    )

    dfs.run()


def continuous_components_test():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': [],
        'D': ['E'],
        'E': []
    }

    positions = calculate_positions(graph)

    cc = ContinuousComponents(graph)
    dfs = cc.run()

    print_graph(
        graph,
        grey_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITING],
        black_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITED],
        positions=positions
    )


# simple_dfs_test()
continuous_components_test()
