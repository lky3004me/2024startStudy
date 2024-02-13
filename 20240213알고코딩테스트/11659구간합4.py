import sys

sys.stdin = open("input.txt" , "r")

n , m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
partSum = [0] * n
sum = 0

for i in range(len(arr)):
    if i == 0:
        partSum[i] = arr[i]    
    else:
        partSum[i] = partSum[i-1] + arr[i]
    
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))    
    
    if tmp[0] == 1:
        print(partSum[tmp[1]-1])
    else:
        print(partSum[tmp[1]-1] - partSum[tmp[0] - 2])

