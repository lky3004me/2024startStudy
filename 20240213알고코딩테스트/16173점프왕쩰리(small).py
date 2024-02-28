import sys

sys.stdin = open("input.txt" , "r")
n = input()
arr = []
arrive = False
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr.append(list(input()))


