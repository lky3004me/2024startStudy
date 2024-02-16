import sys

sys.stdin = open("input.txt" ,"r")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
i =0 
j = n-1

while i <j:
    if arr[i] + arr[j] < m:
        i +=1
    elif arr[i] + arr[j] > m:
        j -=1
    else:
        cnt +=1
        i +=1
        j-=1
    
print(cnt)

