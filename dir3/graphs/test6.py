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

def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for i in graph[node]:
            dfs(graph,i,visited)

dfs(graph,"A",[])