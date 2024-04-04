import sys

sys.stdin = open("input.txt", "r")
n = int(input())
timeTable = []

end = 0
ans = 0

for i in range(n):
    timeTable.append(list(map(int, input().split())))

timeTable.sort(key=lambda x: (x[1], x[0]))

for a, b in timeTable:
    if end <= a:
        ans +=1
        end = b

print(timeTable)