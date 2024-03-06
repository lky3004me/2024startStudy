from collections import deque

import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, 0,-1, 0]
dy = [0, 1, 0, -1]
rst =[]
for i in range(n):
    graph.append(list(map(int, input().split())))


ans = 0
items = 0
def bfs(x, y):
    q = deque()
    cnt = 0

    q.append((x, y))
    while q:
        nx, ny = q.popleft()
        if graph[ny][nx] == 0 or visited[ny][nx]:
            continue

        visited[ny][nx] = True
        cnt+=1
        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < m and 0<= cy < n :
                if visited[cy][cx]!=0 and graph[cy][cx] == 1:
                    q.append((cx,cy))
                    cnt +=1
    
    return cnt
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        x, y = j, i
        num = bfs(x,y)
        print(f"num -> {num}")
        if num !=0:
            ans = num if ans < num else ans
            items = items + 1
        ans = num if ans < num else ans


print(items)
print(ans)
                
                



