from collections import deque
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
deq = deque(list(map(int, input().split())))
res=[]
print(deq)

idx = deq.popleft()
res.append(1)

for i in range(N):
    if idx > 0:
        for _ in range(idx-1):
            deq.append(deq.popleft())
    else:
        for _ in range(abs(idx) - 1):
            deq.appendleft(deq.pop())

    idx = deq.popleft()
    tmp = res[-1] + idx
    if tmp > 5:
        tmp -=5
    elif tmp < 0:
        tmp = tmp + 5
    res.append(idx)
print(res)