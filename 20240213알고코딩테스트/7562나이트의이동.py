from collections import deque

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return matrix[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<i and 0<=ny<i and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] +1
                q.append((nx,ny))

for _ in range(t):
    i = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    matrix = [[0] * i for _ in range(i)]
    matrix[sx][sy] = 1
    print(bfs())

