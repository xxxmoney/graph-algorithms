from dfs import DepthFirstSearch
from dfs import VertexState
from print_graph import print_graph

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

positions = {
    'A': (0, 0),
    'B': (-1, -1),
    'C': (-2, -2),
    'D': (-1, -2),
    'E': (0, -2),
    'F': (1, -2),
    'G': (1, -1),
    'H': (2, -1),
    'I': (3, -1)
}

dfs = DepthFirstSearch(graph)

dfs.on_change(
    lambda: print_graph(
        graph,
        grey_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITING],
        black_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITED],
        positions=positions)
)

dfs.run()
