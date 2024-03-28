import sys
from queue import PriorityQueue

sys.stdin = open("input.txt", "r")
n = int(input())
pq = PriorityQueue()

for _ in range(n):
    data = int(input())
    pq.put(data)

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    tmp = data1 + data2
    sum += tmp
    pq.put(tmp)

print(sum)