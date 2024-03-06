from collections import deque

import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

rst = [0]
dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    global visited
    q = deque()
    cnt = 0

    if graph[y][x] == 0 or visited[y][x]:
        return 0

    q.append((x,y))
    while q:
        nx, ny = q.popleft()

        if visited[ny][nx]:
            continue
        
        cnt +=1
        visited[ny][nx] = True
        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0<= cx <m and 0 <= cy < n:
                if not visited[cy][cx] and graph[cy][cx] != 0:
                    q.append((cx, cy))

    return cnt

for i in range(n):
    for j in range(m):
        x,y = j, i
        num = bfs(x, y)

        if num != 0:
            rst.append(num)
rst.sort()
print(len(rst) - 1)
print(max(rst))