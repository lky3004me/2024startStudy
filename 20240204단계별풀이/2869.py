import sys

sys.stdin = open("input.txt" ,"r")
a,b,v = map(int, sys.stdin.readline().split())

target = v - a
cnt = 0

if target % (b-a) == 0:
    cnt = target//(a-b) +1
else:
    cnt = target//(a-b) +2

print(cnt)




