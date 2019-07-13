import reprlib
from typing import TypeVar

T = TypeVar('T', bound='Node')


class Node:
    def __init__(self, name: str):
        self._name = name
        self.children = list()

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Node(name={name}, children={child_names})'.format(
            name=self.name,
            child_names=reprlib.repr([c.name for c in self.children])
        )

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def _init_graph(data):
    nodes = {k: Node(k) for k in data.keys()}

    for node_name, children in data.items():
        node = nodes[node_name]
        for child_name in children:
            node.children.append(nodes[child_name])

    root = next(iter(nodes.values()))
    return root


# ../images/graph_cycle.png
def init_cycle_graph():
    data = {
        'A': ('B', 'C', 'D'),
        'B': ('E',),
        'C': ('D', 'G'),
        'D': ('L', 'J'),
        'E': ('F',),
        'F': ('G',),
        'G': ('B',),
        'H': ('G',),
        'J': ('H',),
        'L': ('C',),
    }

    return _init_graph(data)


# ../images/graph.png
def init_graph():
    data = {
        'A': ('B', 'C', 'D'),
        'B': ('H', 'I', 'F', 'E'),
        'C': ('J', 'K', 'F', 'G'),
        'D': ('L', 'M', 'E', 'G'),
        'E': ('I',),
        'F': ('J',),
        'G': ('L',),
        'H': ('J',),
        'I': (),
        'J': (),
        'K': ('L',),
        'L': (),
        'M': ('I',),
    }
    return _init_graph(data)


# ../images/tree.png
def init_tree():
    data = {
        'A': ('B', 'C'),
        'B': ('D', 'E'),
        'C': ('F', 'G'),
        'D': (),
        'E': ('H',),
        'F': (),
        'G': ('I',),
        'H': (),
        'I': (),
    }
    return _init_graph(data)
