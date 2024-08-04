from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 미로 크기 및 기본 요금, 추가 요금, 통행료 입력 받기
n, m = map(int, input().split())
x, y, z = map(int, input().split())

# 미로 그래프 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 경로 입력 받기
routes = []
for i in range(m):
    a, b, c, d = map(int, input().split())
    routes.append((a, b, c, d))

# BFS 함수 정의
def bfs(maze, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(maze)
    
    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == goal:
            return distance[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
    
    return -1

# 각 경로에 대해 이동 거리 계산 및 비용 계산
for a, b, c, d in routes:
    # 좌표는 1부터 시작하므로 0 기반 인덱스로 변환
    distance = bfs(graph, (a, b), (c, d))
    
    if distance == -1:
        print("목표 지점에 도달할 수 없습니다.")
    else:
        if distance > 5:
            total_cost = x + (distance - 5) * y + distance * z
        else:
            total_cost = x - distance * z
        
        print(total_cost)
