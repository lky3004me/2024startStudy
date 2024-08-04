import sys

sys.stdin = open("input.txt", "r")
t = int(input())
for i in range(t):
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(2)]
    arr = []
    for a in range(2):
        arr.append(list(map(int, input().split())))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n ==1 :
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n ==2 :
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]
    
    print(max(dp[0][-1], dp[1][-1]))
    
    

    