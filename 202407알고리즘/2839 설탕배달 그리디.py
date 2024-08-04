import sys
sys.stdin = open("input.txt", "r")

n = int(input())

dp = [0]*2
dp[0] = n // 5
ans = []

if (n % 5) % 3 == 0:
    dp[1] =  (n % 5) // 3
    ans.append(dp[0] + dp[1])
else:
    for i in range(dp[0]-1, 0 , -1):
        #i는 5가 차지하는 자리
        if (n - i*5) % 3 == 0:
            dp[0] = i
            dp[1] = (n - i*5) // 3

            ans.append(dp[0] + dp[1])
            break
    
    dp[0] = n//3
    for i in range(1, dp[0]+1):
        if(n-i*3)%5 ==0:
            dp[0] = i
            dp[1] = (n-dp[0]*3) //5

            ans.append(dp[0] + dp[1])
            break

    if(n % 3 == 0):
        ans.append(n//3)

if(len(ans) == 0):
    print(-1)
else:
    print(min(ans))


    
