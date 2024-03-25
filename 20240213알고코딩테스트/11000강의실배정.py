import sys
import heapq

if __name__ == "__main__":
    n = int(input())
    schList= [list(map(int,input().split())) for _ in range(n)]
    schList.sort()

    pq = list()
    heapq.heappush(pq, schList[0][1])

    for i in range(1,n):
        if schList[i][0] >= pq[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, schList[i][1])

    print(len(pq))

