from collections import deque

from graphs import Node, init_tree, init_graph, init_cycle_graph


def bfs_tree(root: Node, searched):
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node.name == searched:
            return node

        dq += node.children


def bfs_graph(root: Node, searched):
    dq = deque([root])
    visited = set()

    while dq:
        node = dq.popleft()
        if node not in visited:
            if node.name == searched:
                return node

            visited.add(node)

            dq += node.children


def tree():
    root = init_tree()
    searched = 'G'
    g = bfs_tree(root, searched)
    assert g.name == searched


def graph():
    root = init_graph()
    searched = 'H'
    h = bfs_graph(root, searched)
    assert h.name == searched


def cycle():
    root = init_cycle_graph()
    searched = 'F'
    f = bfs_graph(root, searched)
    assert f.name == searched


def main():
    tree()
    graph()
    cycle()


if __name__ == '__main__':
    main()
