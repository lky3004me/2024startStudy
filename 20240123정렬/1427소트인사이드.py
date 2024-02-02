import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr =[]
judge = 10

while True:
    arr.append(n%judge)
    n //=10

    if n == 0 :
        break

arr.sort(reverse=True)
print(*arr, sep="")
