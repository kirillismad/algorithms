# def find_lowest_cost_node(costs):
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#
#     return lowest_cost_node


#
# graph = {
#     'start': {'a': 6, 'b': 2},
#     'a': {'fin': 1},
#     'b': {'a': 3, 'fin': 5},
#     'fin': {}
# }
#
# inf = float('inf')
# costs = {'a': 6, 'b': 2, 'fin': inf}
#
# parents = {'a': 'start', 'b': 'start', 'fin': None}
#
# processed = []
#
# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
#
# print(costs)
# print(parents)

adj_matrix = [
    [0, 2, 6, 0],
    [0, 0, 3, 5],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]


def _get_v(v):
    if v == 0:
        return float('inf')
    return v


def _get_graph(matrix):
    r = {}
    for i, row in enumerate(matrix):
        r[i] = {i: value for i, value in enumerate(row) if value != 0}
    return r

    # return {i: {{i: value for i, value in enumerate(row) if value != 0}} for i, row in enumerate(matrix)}


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra(adj_matrix, start_index, end_index):
    costs = {i: _get_v(x) for i, x in enumerate(adj_matrix[start_index]) if i != start_index}
    parents = {k: start_index for k, v in costs.items() if v != float('inf')}
    graph = _get_graph(adj_matrix)
    processed = set()

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)

    p = parents[end_index]
    lst = [end_index, p]
    while True:
        p = parents.get(p)
        if p is None:
            break
        lst.append(p)
    lst.reverse()
    return lst, costs[end_index]


def main():
    r = dijkstra(adj_matrix, 0, 3)

    que, cost = r
    print(que, cost)


if __name__ == '__main__':
    main()
