import sys

sys.stdin = open("input.txt" ,"r")

n = int(sys.stdin.readline())
ai = list(map(int, sys.stdin.readline().split()))
ai.sort()
rst = 0
cnt = 0

for k in range(n):
    find = ai[k]
    i = 0
    j = n-1
    while i < j:
        if ai[i] + ai[j] == find:
            if i != k and j != k:
                rst +=1
                break
            elif i == k:
                i +=1
            elif j == k:
                j -=1
        elif ai[i] + ai[j] <find:
            i +=1
        else:
            j -=1
print(rst)
            
