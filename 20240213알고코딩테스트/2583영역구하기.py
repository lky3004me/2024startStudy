import sys
sys.setrecursionlimit(100000)

sys.stdin = open("input.txt" , "r")
#m이 세로, n이 가로
visit=[]
occupied = []
rst = []
m,n,k = map(int, input().split())
cnt = 0
max = 0

occupied = [[False for _ in range(n)] for _ in range(m)]
visit = [[False for _ in range(n)] for _ in range(m)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for j in range(ly, ry):
        for k in range(lx, rx):
            occupied[j][k] = True
    
def DFS(x, y):
    global cnt
    global visit
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif occupied[y][x] or visit[y][x]:
        return False
    
    cnt +=1 
    visit[y][x] = True
    
    DFS(x-1, y)
    DFS(x, y-1)
    DFS(x+1, y)
    DFS(x, y+1)

    return True


for i in range(m):
    for j in range(n):
        y = i
        x = j
        
        if DFS(x,y):
            rst.append(cnt)
            max +=1
            cnt =0

rst.sort()

print(max)
print(*rst, sep=" ")
        


    

