import sys

n = int(sys.stdin.readline())
cnt = 1
sum = 1
sIdx = 1
eIdx = 1

while eIdx != n:
    if sum == n:
        cnt +=1
        eIdx +=1
        sum += eIdx
    elif sum > n:
        sum -= sIdx
        sIdx +=1
    else:
        eIdx +=1
        sum += eIdx

print(cnt)    
    