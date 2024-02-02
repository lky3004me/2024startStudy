#https://gudwns1243.tistory.com/52

import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

compArr = sorted(list(set(arr)))

#시간초과 
# for org in arr:
#     for j in range(len(compArr)):
#         if org == compArr[j]:
#             print(j, end=' ')
#             break

dic = {compArr[i]: i for i in range(len(compArr))}
for i in arr:
    print(dic[i], end=' ')

