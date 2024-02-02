import sys

sys.stdin = open("input.txt", "r")
arr = []

n = int(sys.stdin.readline())

for i in range(n):
    arr.append(sys.stdin.readline().strip())

set_arr = set(arr)
rst = list(set_arr)
rst.sort()
rst.sort(key=len)

for ele in rst:
    print(ele)