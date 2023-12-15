from abc import ABC, abstractmethod


# define APIs for accessing Graph
class BaseGraphService(ABC):
    # add an edge into graph with node pair (from, to)
    @abstractmethod
    def add_edge(self, from_node, to_node):
        raise NotImplementedError()

    # remove an edge from graph with node pair (from, to) if exists
    @abstractmethod
    def remove_edge(self, from_node, to_node):
        raise NotImplementedError()

    # return a specified node from graph if exists
    @abstractmethod
    def get_node(self, node):
        raise NotImplementedError()

    # return a sub graph with a specified node
    @abstractmethod
    def get_sub_graph(self, center_node):
        raise NotImplementedError()
