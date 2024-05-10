import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                queue.append(i)
            elif visited[i] == visited[a]:
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = True
    for i in range(1, v+1):
        if not visited[i]:
            if not bfs(i):
                result = False
                break
    print('YES' if result else 'NO')
