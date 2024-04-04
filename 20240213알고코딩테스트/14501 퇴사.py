import sys

sys.stdin = open("input.txt" , "r")

n = int(input())
tArr = [0]
pArr = [0]
dp = [0 for _ in range(n+2)]

for i in range(1, n+1):
    t, p = map(int, input().split())

    tArr.append(t)
    pArr.append(p)

for i in range(n,0,-1):
    if i + tArr[i] > n +1 :
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pArr[i] + dp[i + tArr[i]])

print(dp[i])
                    
    
