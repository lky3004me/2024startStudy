import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
comp = list(map(int, input().split()))
find = False

def binS(target):    
    s  = 0
    e = len(arr)-1

    while s <= e:
        midi = int((s + e) / 2)
        midv = arr[midi]

        if midv > target:
            e = midi - 1
        elif midv < target:
            s = midi + 1
        else:
            return True

    return False

for target in comp:
    if binS(target):
        print(1)
    else:
        print(0)