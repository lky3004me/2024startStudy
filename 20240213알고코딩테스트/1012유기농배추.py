import sys
sys.setrecursionlimit(10000)
sys.stdin = open("input.txt" , "r")

t = int(input())

def DFS(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if wyrm[y][x] == 1 and not visited[y][x]:
        visited[y][x] = True
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False

for i in range(t):
    m,n,k = map(int, input().split())
    wyrm = [[0 for _ in range(m)] for _ in range(n)]
    visited  = [[False for _ in range(m)] for _ in range(n)] 
    cnt = 0 

    for i in range(k):
        x,y = map(int, input().split())
        wyrm[y][x] = 1

    for j in range(n):
        for k in range(m):
            x = k
            y = j
            if wyrm[j][k] == 1 and not visited[j][k]:
                if DFS(x,y):
                    cnt +=1

    print(cnt)



