import sys
sys.stdin = open("input.txt", "r")

def max_score(scores):
    n = len(scores)
    if n == 0:
        return 0
    elif n ==1:
        return scores[0]
    elif n ==2:
        return scores[0] + scores[1]
    
    dp =[0] *n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1]+scores[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i])

    return dp[-1]


n = int(input())
scores = [0] * (n+1)
for i in range(1, n+1):
    scores[i] = int(input())

print(max_score(scores))
