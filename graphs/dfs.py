from graphs import Node, init_tree, init_graph, init_cycle_graph


def dfs_recursive_tree(root: Node, searched):
    if root.name == searched:
        return root

    for ch in root.children:
        result = dfs_recursive_tree(ch, searched)
        if result is not None:
            return result


def dfs_recursive_graph(root: Node, searched, visited=None):
    if visited is None:
        visited = set()

    if root not in visited:
        if root.name == searched:
            return root

        visited.add(root)
        for ch in root.children:
            result = dfs_recursive_graph(ch, searched, visited)
            if result is not None:
                return result


def tree():
    root = init_tree()
    searched = 'G'
    g = dfs_recursive_tree(root, searched)
    assert g.name == searched


def graph():
    root = init_graph()
    searched = 'G'
    h = dfs_recursive_graph(root, searched)
    assert h.name == searched


def cycle():
    root = init_cycle_graph()
    searched = 'F'
    f = dfs_recursive_graph(root, searched)
    assert f.name == searched


def main():
    tree()
    graph()
    cycle()


if __name__ == '__main__':
    main()
