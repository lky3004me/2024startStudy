import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
rst = [-1] * n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        rst[stack.pop()] = arr[i]
    stack.append(i)

print(*rst)
