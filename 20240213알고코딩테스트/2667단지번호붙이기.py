import sys
sys.setrecursionlimit(10000)

sys.stdin = open("input.txt" , "r")

n = int(input())
graph = []
rst = []
cnt = 0
for i in range(n):
    line = input()
    row = [int(c) for c in line]
    graph.append(row)    
visited = [[False for _ in range(n)] for _ in range(n)]

def DFS(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0

    if graph[y][x] == 1 and not visited[y][x]:
        visited[y][x] = True

        a = DFS(x-1, y)
        b = DFS(x, y-1)
        c = DFS(x+1, y)
        d = DFS(x, y+1)
        return a+b+c+d +1
    return 0

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            sum = DFS(x, y)
            rst.append(sum)
            cnt +=1

rst.sort()

print(cnt)
for ele in rst:
    print(ele)


