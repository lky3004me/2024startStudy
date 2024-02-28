N = int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

base = [[0] * N for _ in range(N)]

def dfs(x,y):

    if x < 0 or x >= N or y < 0 or y >= N or base[x][y] == 1:
        return False
    if graph[x][y] == -1: # 끝
        base[x][y] = 1
        return False
    base[x][y] = 1 # 방문 기록 남기기
    dfs(x+graph[x][y], y)
    dfs(x, y+graph[x][y])

dfs(0,0)
if base[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')