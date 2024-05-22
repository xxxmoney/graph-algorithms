from print_graph import print_graph


def dfs(graph, node, positions=None):
    visited = set()
    stack = []

    print_graph(graph, list(stack), list(visited), positions)

    visited.add(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print_graph(graph, list(stack), list(visited), positions)
        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                stack.append(n)

                print_graph(graph, list(stack), list(visited), positions)
                print('Stack: ', stack)
                print('Visited: ', visited)


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

dfs(graph, 'A', positions=positions)
