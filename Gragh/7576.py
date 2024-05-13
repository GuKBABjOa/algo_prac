from collections import deque

row, col = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(col)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque([])

for i in range(col):
    for j in range(row):
        if tomatoes[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < col and 0 <= ny < row and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in tomatoes:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

result = max(max(i) for i in tomatoes)
print(result - 1)
