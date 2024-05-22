from collections import deque
from print_graph import print_graph

def bfs(graph, node, positions=None):
    visited = set()
    queue = deque()

    print_graph(graph, queue, visited, positions)

    visited.add(node)
    queue.append(node)
    print_graph(graph, queue, visited, positions)

    while queue:
        s = queue.popleft()
        print_graph(graph, queue, visited, positions)

        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

                print_graph(graph, queue, visited, positions)
                print('Queue: ', queue)
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

bfs(graph, 'A', positions=positions)
