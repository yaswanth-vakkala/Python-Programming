def add_node(n):
    global node_count
    if n in node:
        print("node is present")
    else:
        node_count = node_count+1
        node.append(n)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

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
add_node("c")
print("after")
print(node)
print(graph)
matrix()
