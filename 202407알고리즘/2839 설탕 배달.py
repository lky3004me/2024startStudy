import sys
sys.stdin = open("input.txt", "r")

n = int(input())
rst = [99999]
# 1. 먼저 5를 넣고 구하고, 불가하면 3을 조합
# 1-1. 5의 개수를 순차적으로 낮추어서 다른 조합도 찾아야 함.
# 2. 위가 불발시, 3을 넣고 구하고, 불가하면 5를 조합
# 2-2. 3의 개수 또한 순차적으로 낮추어서 다른 조합도 찾아야 함.
# 3. 이렇게 구해진 것들 중 가장 작은 걸 출력 (불가하면 -1을 넣기)

if n % 5 ==0:
    rst.append(n//5)
else:
    if (n%5)%3 ==0:
        tmp1 = n//5
        tmp2 = (n%5)//3
        
        rst.append(tmp1+tmp2)
    else:
        for i in range(1, n//5+1):
            if (n - 5*i)%3 == 0:
                tmp1 = i
                tmp2 = (n-5*i)//3
                rst.append(tmp1+tmp2)

if n % 3 == 0:
    rst.append(n//3)
else:
    if(n%3)%5 ==0:
        tmp1 = n//3
        tmp2 = (n%3)//5

        rst.append(tmp1+tmp2)
    else:
        for i in range(1, n//3+1):
            if (n - 3*i)%5 == 0:
                tmp1 = i
                tmp2 = (n-3*i)//5
                rst.append(tmp1+tmp2)
                
result = min(rst)

if result == 99999:
    print(-1)
else:
    print(result)