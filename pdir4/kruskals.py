def get_min_spanning_tree(graph):
    new_graph = []
    taken = {}
    cost = 0

    while graph:
        curr = graph.pop()

        if taken.get(curr[0], 0) >= 2 or taken.get(curr[1], 0) >= 2:
            continue

        cost += curr[2]
        taken[curr[0]] = taken.get(curr[0], 0) + 1
        taken[curr[1]] = taken.get(curr[1], 0) + 1
        new_graph.append(curr)

    for l, r, w in new_graph:
        print(f"{l} -> {r} : {w}")

    return cost


# if __name__ == '__main__':
    # Adjacency List
    # graph = [(1, 2, 28), (1, 6, 10), (2, 3, 16), (2, 7, 14),
    #          (3, 4, 12), (4, 5, 22), (4, 7, 18), (5, 6, 25), (5, 7,24 )]

graph = [(1,2,1),(1,3,7),(1,4,10),(2,3,3),(3,4,4),(4,5,2)]
# The greedy part
graph.sort(key=lambda x: x[2], reverse=True)
print("The minimum cost is", get_min_spanning_tree(graph))
