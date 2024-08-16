import  sys
sys.stdin = open("input.txt", "r")

n, x = map(int, input().split())
visitors = list(map(int, input().split()))
result = 0
max = 0
cnt = 0
rst = []

#이거 dp 비슷하게 하면 n 나올 것 같은데
# start= 0, end = x-1
# 스타트와 엔드를 하나씨 추가 엔드가 n-1에 도달하면 종료

start = 0
end = x-1

#초기 설정
for i in range(end+1):
    result += visitors[i]
if result > max:
    max = result
    rst.append(result)

#스타트는 이전 값으로 빼버리고, 엔드는 하나 더해서 추가하기
for i in range(n-x):
    result -= visitors[start]
    start +=1

    end +=1
    result += visitors[end]

    if result > max:
        max = result
    rst.append(result)

for i in range(len(rst)):
    if rst[i] == max:
        cnt +=1

if max == 0:
    print("SAD")
else:
    print(max)
    print(cnt)




