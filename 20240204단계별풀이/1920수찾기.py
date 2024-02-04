import sys
sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
nArr = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))

for ele in mArr:
    if ele in nArr:
        print("1")
    else:
        print("0")

#chatgpt에 물어본 in의 시간복잡도 기록

