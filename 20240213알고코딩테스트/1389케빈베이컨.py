from collections import deque

import sys
sys.stdin = open("input.txt", "r")

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
rst = []
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

def bfs(start):
    visited = [0] * (n+1)
    q = deque()    
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()

        for ele in adj[now]:
            if not visited[ele]:
                visited[ele] = visited[now] + 1
                q.append(ele)
    return sum(visited)
    
for i in range(1, n+1):
    rst.append(bfs(i))

min_value = min(rst)
min_idx = [i for i, value in enumerate(rst) if value == min_value]

sIdx = min(min_idx)
print(sIdx + 1)