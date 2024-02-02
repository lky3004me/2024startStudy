import sys

sys.stdin = open("input.txt", "r")
arr = []

while True:
    line = sys.stdin.readline().strip()
    print(line)

    if not line:
        break
