from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start_x, start_y):
    queue = deque([[start_x, start_y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] == 1:
                queue.append([next_x, next_y])
                maze[next_x][next_y] = maze[x][y] + 1

bfs(0, 0)
print(maze[n - 1][m - 1])
