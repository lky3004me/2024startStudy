import sys

sys.stdin = open("input.txt", "r")
    
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    arr = [x for x in range(1, n+1)]
    for j in range(k):
        for k in range(1, n):
            arr[k] += arr[k-1]

    print(arr[-1])
