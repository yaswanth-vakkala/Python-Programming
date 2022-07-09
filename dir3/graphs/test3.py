def add_node(n):
    global node_count
    if n in node:
        print("given node is already present")
    else:
        node_count = node_count+1
        node.append(n)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def edge(n1,n2):
    if n1 not in node:
        print(n1,"does not exist")
    elif n2 not in node:
        print(n2,"does not exist")
    else:
        i1 = node.index(n1)
        i2 = node.index(n2)
        graph[i1][i2] = 1
        # graph[i2][i1] = 1

def matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()


node = []
graph = []
node_count = 0
print("before")
print(node)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
print("after")
print(node)
print(graph)
matrix()
print("_______")
edge("C","D")
edge("A","C")
print(node)
print(graph)
matrix()

