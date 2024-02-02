import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
noL = []
noS = []
cnt = 0
rst = []
idx = -1

for i in range(n):
    noL.append(sys.stdin.readline().strip())
    
for j in range(m):
    noS.append(sys.stdin.readline().strip())
    
for ele in noL:
    try:
        idx = noS.index(ele)
    except:
        pass
    
    if idx != -1:
        tmp = noS.pop(idx)
        rst.append(tmp)
        cnt +=1
        idx = -1
        
print(cnt)
for ele in rst:
    print(ele)   


#1초면 1억정도. 