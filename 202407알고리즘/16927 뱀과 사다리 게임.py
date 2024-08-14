import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
leather = []
snake = []

for i in range(n):
    x, y = map(int, input().split())
    leather.append([x, y])

for i in range(m):
    u, v= map(int, input().split())
    snake.append([u, v])

leather.sort()
print(leather)

# 일단 사다리 정렬 필요
# 고민 1: 뱀은 완전 제외인가
# 고민 2: 사다리를 가장 가까운 걸 타지 않고 다음 번을 탔을 때 더 빠르다면 그걸 어떻게 고려할 것인가

# 발상 1 : 브루트 포스 병신임
# 발상 2 : dp 느낌이 나는데 
