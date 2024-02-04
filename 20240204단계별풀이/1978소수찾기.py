import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr= list(map(int, sys.stdin.readline().split()))
cnt = n

for ele in arr:
    if ele < 2:
        cnt -=1
        continue

    for i in range(2, int(ele**0.5) + 1):
        if ele % i == 0:
            cnt -= 1
            break
    
    
print(cnt)    
