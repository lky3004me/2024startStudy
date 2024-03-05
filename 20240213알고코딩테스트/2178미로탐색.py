from collections import deque

import sys
sys.stdin = open("input.txt", "r")
dx = [0,1,0,-1]
dy = [1,0,-1,0]
n,m = map(int, input().split())
arr = [[0] *m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        arr[i][j] = int(numbers[j])

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[1] + dx[k]
            y = now[0] + dy[k]

            if x >= 0 and x < m and y >=0 and y < n:
                if arr[y][x] != 0 and not visited[y][x]:
                    visited[y][x] = True
                    arr[y][x] = arr[now[0]][now[1]] +1
                    queue.append((y,x))

BFS(0,0)
print(arr[n - 1][m - 1])