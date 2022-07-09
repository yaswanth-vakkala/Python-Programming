class Stack:
    def __init__(self):
        self.list = []

    def display(self):
        print(self.list)

    def push(self,element):
        self.list.append(element)

    def pop(self):
        if self.list == []:
            return False
        else:
            self.list.pop()

    def peek(self):
        if self.list == []:
            return False
        else:
            return self.list[-1]

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

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

def dfs(visited,graph,node):
    visited.append(node)
    stk.push(node)
    print(stk.peek(), end=" ")
    while stk:
        s = stk.peek()
        flag = 0
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                stk.push(n)
                print(n,end=" ")
                flag = 1
                break
        if flag == 0:
            stk.pop()
        if stk.isempty():
            quit()


stk = Stack()
visited = []
dfs(visited,graph,"A")
