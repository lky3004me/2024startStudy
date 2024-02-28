import sys

sys.stdin = open("input.txt", "r")
n,m = map(int, input().split())
cnt = 0
arr = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr.append(input())

def DFS(x, y):
    visited[x][y] = True
    if arr[x][y] == '|':
        if x +1 < n and arr[x+1][y] == '|' and visited[x+1][y] == False:
            DFS(x+1, y)
        else:
            return
    if arr[x][y] == '-':
        if y+1<m and arr[x][y+1] == '-' and visited [x][y+1] == False:
            DFS(x, y+1)
        else:
            return
    
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            DFS(i,j)
            cnt +=1

print(cnt)

