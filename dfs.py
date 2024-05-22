from events import Events
from enum import Enum


class VertexState(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class DepthFirstSearch:
    def __init__(self, graph, order=None):
        self.graph = graph
        self.states = {vertex: VertexState.UNVISITED for vertex in graph}
        self.time = 0
        self.times = {vertex: (0, 0) for vertex in graph}
        self.__events = Events()
        self.order = order if order else [vertex for vertex in graph]

    def run(self):
        self.__call_on_change()

        for vertex in self.order:
            if self.states[vertex] == VertexState.UNVISITED:
                self.visit(vertex)

        self.__call_on_change()

    def visit(self, vertex):
        self.states[vertex] = VertexState.VISITING
        self.time += 1
        self.times[vertex] = (self.time, 0)

        self.__call_on_change()

        for neighbor in self.graph[vertex]:
            if self.states[neighbor] == VertexState.UNVISITED:
                self.visit(neighbor)

        self.states[vertex] = VertexState.VISITED
        self.time += 1
        self.times[vertex] = (self.times[vertex][0], self.time)
        self.__call_on_change()

    def on_change(self, callback):
        self.__events.on_change += callback

    def __call_on_change(self):
        self.__events.on_change()
