import sys
sys.stdin = open("input.txt", "r")

global graph
graph = [[0 for _ in range(100)] for _ in range(100)]

def paint(x, y):
    endX = x + 10
    endY = y + 10

    for i in range(0, 10):
        for j in range(0, 10):
            graph[y + i][x + j] = 1

def cal():
    cnt = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if(graph[i][j] == 1):
                cnt +=1

    return cnt


n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    paint(x,y)

print(cal())

    