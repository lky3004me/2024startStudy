import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

arr.sort(key=lambda x: ( int(x[0])))

for ele in arr:
    print(*ele, sep=" ")