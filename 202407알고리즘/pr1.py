#문제 -> mkdir, cd, cd.. 가 주어지고 최후에 배열 출력시 dir 구조 나오는 것. 

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
dir = [[] for _  in range(n)]
targetLine = -1
point = 0

for i in range(n):
    commandInput = input().split()

    if commandInput[0] == "mkdir":
        if point == 0:
            
            dir.append(commandInput[1])
        else:
            dir[point].append(commandInput[1])
    elif commandInput[0] == "cd":
        #대상 줄이 없음
        if targetLine == -1:
            for j in range(n):
                if dir[j][0] == commandInput[1]:
                    dir[j].append(commandInput[1])
                    targetLine = j
                    point +=1
        #대상 줄이 있음
        else:
            for j in range(n):
                if dir[targetLine][point] == commandInput[1]:
                    dir[targetLine].append(commandInput[1])
                    point +=1

    elif commandInput[0] == "cd..":
        if point == 1:
            targetLine = -1
            point -=1
        else:
            point -=1

print(dir)
        

    