import networkx as nx
import matplotlib.pyplot as plt
from calculate_positions import calculate_positions
from dfs import VertexState


def print_graph(graph, grey_nodes=None, black_nodes=None, positions=None):
    if grey_nodes is None:
        grey_nodes = []
    if black_nodes is None:
        black_nodes = []
    if positions is None:
        positions = nx.spring_layout(graph)

    print('grey_nodes:', grey_nodes)
    print('black_nodes:', black_nodes)

    G = nx.DiGraph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    node_colors = ['grey' if node in grey_nodes else ('black' if node in black_nodes else 'white') for node in
                   G.nodes()]
    nx.draw(G, pos=positions, with_labels=True, node_color=node_colors, font_color='red', font_weight='bold', )
    plt.show()
    plt.close()


def print_graph_from_dfs(graph, dfs):
    positions = calculate_positions(graph)

    print_graph(
        graph,
        grey_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITING],
        black_nodes=[vertex for vertex, state in dfs.states.items() if state == VertexState.VISITED],
        positions=positions
    )
