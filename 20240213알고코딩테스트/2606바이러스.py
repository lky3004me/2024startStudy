import sys
sys.stdin = open("input.txt" , "r")

n = int(input())
m = int(input())

adj = [[] for m in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    n1,n2 = map(int, input().split())
    
    adj[n1].append(n2)
    adj[n2].append(n1)

def DFS(v):
    global cnt
    visited[v] = True
    cnt +=1
    for i in adj[v]:
        if not visited[i]:
            DFS(i)


DFS(1)

print(cnt-1)