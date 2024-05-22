import networkx as nx


def calculate_positions(graph):
    G = nx.DiGraph(graph)
    return nx.circular_layout(G)
