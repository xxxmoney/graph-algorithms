from dfs import DepthFirstSearch, EdgeType
from transpose import transpose


class ContinuousComponents:
    dfs = None
    dfs_transposed = None

    def __init__(self, graph):
        self.graph = graph

    def run(self):
        self.dfs = DepthFirstSearch(self.graph)
        self.dfs.run()

        transposed = transpose(self.graph)
        order = sorted(self.dfs.times, key=lambda vertex: self.dfs.times[vertex][1], reverse=True)
        self.dfs_transposed = DepthFirstSearch(transposed, order)
        self.dfs_transposed.run()

        return ContinuousComponents.__find_sccs_from_edges(self.dfs_transposed)

    @staticmethod
    def __find_sccs_from_edges(dfs):
        sccs = []
        visited = set()

        for vertex in dfs.graph:
            if vertex not in visited:
                scc = []
                stack = [vertex]

                while stack:
                    v = stack.pop()
                    visited.add(v)
                    scc.append(v)

                    for neighbor in dfs.graph[v]:
                        edge_type = dfs.edges.get((v, neighbor))
                        if edge_type in {EdgeType.TREE, EdgeType.BACK} and neighbor not in visited:
                            stack.append(neighbor)

                sccs.append(scc)

        return sccs
