import sys
sys.stdin = open("input.txt")

ans = 0
arr = list(map(str, input().split('-')))

def mySum(i):
    sum = 0
    tmp = str(i).split('+')
    for i in tmp:
        sum += int(i)
    return sum

for i in range(len(arr)):
    tmp = mySum(arr[i])
    if i == 0:
        ans +=tmp
    else:
        ans -= tmp

print(ans)