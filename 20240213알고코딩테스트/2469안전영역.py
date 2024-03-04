import sys
sys.setrecursionlimit(10**5)

sys.stdin = open("input.txt", "r")
n = int(input())
arr = []
max = 0
visit = []
height = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def DFS(x, y):
    global visit

    if x < 0 or x >= n or y <0 or y>=n :
        return False
    elif height[y][x] == False or visit[y][x] == True:
        return False
    
    visit[y][x] = True
    DFS(x+1, y)
    DFS(x-1, y)
    DFS(x, y-1)
    DFS(x, y+1)

    return True

for i in range(1, 101):
    visit = [[False for _ in range(n)] for _ in range(n)]
    height = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] >= i:
                height[j][k] = True

    for j in range(n):
        for k in range(n):
            x = k
            y = j
            if DFS(x, y):
                cnt +=1
        
    if cnt > max:
        max = cnt


print(max)

        

