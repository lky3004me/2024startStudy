import sys
from queue import PriorityQueue
from collections import deque

sys.stdin = open("input.txt", "r")
n = int(input())
pq = PriorityQueue()
plus = deque()
rst = []

for _ in range(n):
    pq.put(int(input()))

while pq.qsize()>1:
    a = pq.get()
    b = pq.get()

    if a < 0 and b <= 0:
        rst.append(a*b)
    elif a < 0 and b > 0:
        rst.append(a)
        plus.append(b)
    elif a == 0 and b > 0:
        rst.append(a)
        rst.append(b)
    else:
        plus.append(a)
        plus.append(b)
if pq.qsize() == 1:
    a = pq.get()
    if a <= 0:
        rst.append(a)
    else:
        plus.append(a)

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    if a*b > a+b:
        rst.append(a*b)
    else:
        rst.append(a+b)
if len(plus) == 1:
    rst.append(plus.pop())

print(sum(rst))
