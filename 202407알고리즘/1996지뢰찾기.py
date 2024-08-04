import sys
sys.stdin = open("input.txt", "r")

n = int(input())
graph = []
dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

# 입력 처리
for i in range(n):
    row = input().strip()
    graph.append([int(char) if char.isdigit() else 0 for char in row])

# 원본 그래프 저장
origin = [row[:] for row in graph]

# 주변 8방향을 확인하여 폭탄 위치 업데이트
for i in range(n):
    for j in range(n):
        if isinstance(origin[i][j], int) and origin[i][j] > 0:
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] == 'M':
                        continue
                    sum_val = graph[ni][nj] + origin[i][j]
                    if sum_val >= 10:
                        graph[ni][nj] = 'M'
                    else:
                        graph[ni][nj] = sum_val

# 폭탄 위치 복원
for i in range(n):
    for j in range(n):
        if origin[i][j] > 0:
            graph[i][j] = '*'

# 결과 출력
for row in graph:
    print(''.join(str(cell) for cell in row))
