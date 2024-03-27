import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
arr = []
sum = 0
for _ in range(n):
    arr.append(int(input()))

for ele in reversed(arr):
    if ele <= k:
        print(ele)
        sum += k//ele
        k = k - k*ele

print(sum)
