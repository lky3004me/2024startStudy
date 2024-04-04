import sys

sys.stdin = open("input.txt", "r")

n = int(input())
dp = [[0 for _ in range(2)] for _ in range(n+1)]

for i in range(n):
    if i == 0:
        dp[i][0] = 0
        dp[i][1] = 1
        continue

    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(dp[i][0] + dp[i][1])

    


    