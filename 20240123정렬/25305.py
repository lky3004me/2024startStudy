import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[k-1])
