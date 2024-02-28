import sys
sys.setrecursionlimit(10000)

sys.stdin = open("input.txt", "r")

graph = []
visited = []

def DFS(x,y):
    if x < 0 or x >=w or y<0 or y>= h:
        return False
    
    if graph[y][x] == 1 and not visited[y][x]:
        visited[y][x] = True
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        DFS(x+1, y+1)
        DFS(x+1, y-1)
        DFS(x-1, y+1)
        DFS(x-1, y-1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h ==0:
        break
    
    cnt = 0
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            x = j
            y = i
            if not visited[y][x]  and graph[y][x] == 1:
                if DFS(x, y):
                    cnt +=1

    print(cnt)
     
