import sys

A, B = sys.stdin.readline().split()

a, b = int(A[::-1]), int(B[::-1])

if a < b:
    print(b)
else:
    print(a)
