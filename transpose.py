def transpose(graph):
    transposed = {vertex: [] for vertex in graph}

    for vertex in graph:
        for neighbor in graph[vertex]:
            transposed[neighbor].append(vertex)

    return transposed
