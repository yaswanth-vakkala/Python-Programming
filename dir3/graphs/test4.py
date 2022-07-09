graph = {
    'H':["A"],
    "A":["D","B"],
    "B":["C","F"],
    "C":["G","H"],
    "D":["F"],
    "F":["A"],
    "E":["B"],
    "G":["H","E"],
}

# graph = {
#     "A":["E","D","B"],
#     "B":["A",'C','E'],
#     'C':['B','E','F','G'],
#     'D':['A','E'],
#     'E':['A','B','C','D','F'],
#     'F':['C','E','G'],
#     'G':['C','F'],
# }

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

visited = []
queue = []
bfs(visited,graph,"A")
