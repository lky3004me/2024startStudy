# import sys

# sys.stdin = open("input.txt", "r")
# n = int(sys.stdin.readline())
# wList = []
# nList = []
# isConnect = True
# cnt = 0

# for i in range(n):
#     wList.append(sys.stdin.readline().strip())

# for ele in wList:
#     for i in range(len(ele)):
#         if i == 0:
#             nList.append(ele[i])
#         elif ele[i] != nList[-1]:
#             nList.append(ele[i])        

#     for i in range(len(nList)):
#         if i < len(nList)-1 and nList[i] in nList[i+2:]:
#             isConnect = False
#             break
    
#     if isConnect:
#         cnt +=1

#     isConnect = True
#     nList = []

# print(cnt)

N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)