import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())
deq = deque([i for i in range(1, N+1)])

while(len(deq)>1):
    deq.popleft()
    ret = deq.popleft()
    deq.append(ret)

print(deq[0])


