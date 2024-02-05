import sys

sys.stdin = open("input.txt", "r")
while True:
    a,b,c= map(int, sys.stdin.readline().split())

    if a == b == c == 0:
        break
    if c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == c**2 + b**2:
        print("right")
    else:
        print("wrong")

