import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
candidate = list(map(int, sys.stdin.readline().split()))

cnt = {}

for card in cards:
    if card in cnt:
        cnt[card] +=1
    else:
        cnt[card] = 1

for target in candidate:
    rst = cnt.get(target)
    if rst == None:
        print(0, end=" ")
    else:
        print(rst, end=" ")