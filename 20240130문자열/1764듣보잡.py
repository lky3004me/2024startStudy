import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
noL = []
noS = []
cnt = 0
rst = []

for _ in range(n):
    noL.append(sys.stdin.readline().strip())
    
for _ in range(m):
    noS.append(sys.stdin.readline().strip())
    

noL = {value: index for index, value in enumerate(noL)}

for ele in noS:
    if ele in noL:
        cnt +=1
        rst.append(ele)
        
rst.sort()
print(len(rst))
for ele in rst:
    print(ele)   

#N= 1억이면 1초
#리스트, dict의 시간복잡도 표 가져오기