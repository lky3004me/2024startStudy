import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
deq = deque()
for i in range(1, n+1):
    deq.append(i)

while len(deq) != 1:
    deq.popleft()
    tmp = deq.popleft()

    deq.append(tmp)

print(deq.pop())
