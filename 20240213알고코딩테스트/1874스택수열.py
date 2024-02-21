import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append((int(input()), i))

max = 0
sortedA = sorted(arr)

for i in range(n):
    if max < sortedA[i][1] - i:
        max = sortedA[i][1] -1

print(max +1)