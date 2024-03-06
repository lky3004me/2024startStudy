from collections import deque

import sys
sys.stdin = open("input.txt", "r")

f,s,g,u,d = map(int, input().split())

def bfs():
    visited = [0] * (f +1)
    cnt = [0] * (f +1)
    q = deque()

    q.append(s)
    visited[s] = 1
    while q:
        now = q.popleft()
        
        if now == g:
            print(cnt[g])
            return
        for ele in (now+u, now-d):
            if 0 < ele <= f and not visited[ele]:
                visited[ele] = 1
                cnt[ele] = cnt[now] +1
                q.append(ele)
    
    if visited[g] == 0:
        print("use the stairs")

bfs()
        

    


