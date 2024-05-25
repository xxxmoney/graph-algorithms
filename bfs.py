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
