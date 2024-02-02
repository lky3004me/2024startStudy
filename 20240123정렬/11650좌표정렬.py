import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# for i in range(0, n-1):
#     for j in range(i+1, n):
#         if arr[i][0] > arr[j][0]:
#             arr[i], arr[j] = arr[j], arr[i]

# for a in range(0, n-1):
#     for b in range(a+1, n):
#         if arr[a][1] > arr[b][1]:
#             arr[a], arr[b] = arr[b], arr[a]

arr.sort()
for rst in arr:
    print(*rst, sep=" ")