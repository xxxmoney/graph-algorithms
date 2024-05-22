﻿import networkx as nx
import matplotlib.pyplot as plt


def print_graph(graph, grey_nodes=None, black_nodes = None, positions = None):
    if grey_nodes is None:
        grey_nodes = []
    if black_nodes is None:
        black_nodes = []
    if positions is None:
        positions = nx.spring_layout(graph)

    print('grey_nodes:', grey_nodes)
    print('black_nodes:', black_nodes)

    G = nx.Graph(graph)
    node_colors = ['grey' if node in grey_nodes else ('black' if node in black_nodes else 'white') for node in G.nodes()]
    nx.draw(G, pos=positions, with_labels=True, node_color=node_colors)
    plt.show()
    plt.close()
