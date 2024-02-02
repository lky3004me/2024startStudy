import sys
sys.stdin = open("input.txt", "r")

N = int(input())
numList = list(map(int, input().split()))
myStack = []
target = 1

for i in range(N):
    if target == numList[0]:
        numList.pop(0)
        target+=1
    elif len(myStack) != 0 and target == myStack[-1]:
        myStack.pop(-1)
        target+=1
    else:
        myStack.append(numList.pop(0))
        if len(myStack) > 2 and myStack[-1] > myStack[-2]:
            print("Sad")
            sys.exit()

print("Nice")

