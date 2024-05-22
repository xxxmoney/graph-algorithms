from dfs import DepthFirstSearch
from transpose import transpose


class ContinuousComponents:
    def __init__(self, graph):
        self.graph = graph

    def run(self):
        dfs = DepthFirstSearch(self.graph)
        dfs.run()

        transposed = transpose(self.graph)
        order = sorted(dfs.times, key=lambda vertex: dfs.times[vertex][1], reverse=True)
        dfs_transposed = DepthFirstSearch(transposed, order)
        dfs_transposed.run()

        return dfs_transposed
