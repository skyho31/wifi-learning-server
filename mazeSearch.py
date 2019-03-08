
maze = [[0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 0, 0]]

endPoint = (3, 3)

min = 10000

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x, y):
        self.data.append((x, y))

    def pop(self):
        del self.data[len(self.data) - 1]

    def printContent(self):
        for coordinate in self.data:
            print(str(coordinate[0]) + " " + str(coordinate[1]))

stack = Stack()

def dfs(r, c, d):
    global min
    tr = 0
    tc = 0

    maze[r][c] = 1
    stack.push(r, c)
    for i in range(0, 4):
        tr = r + dr[i]
        tc = c + dc[i]

        if tr >= 0 and tr < len(maze) and tc >= 0 and tc < len(maze[0]):
            if tr == endPoint[0] and tc == endPoint[1]:
                if d < min:
                    min = d
                stack.pop()
                maze[r][c] = 0
                return
            if maze[tr][tc] == 0:
                dfs(tr, tc, d + 1)

#    stack.pop()
    maze[r][c] = 0

dfs(0, 0, 0)

stack.printContent()
