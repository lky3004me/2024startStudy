import sys

sys.stdin = open("input.txt", "r")
while True:
    n = sys.stdin.readline().strip()

    if int(n) == 0:
        break

    if int(n) <10:
        print("yes")
        continue
    for i in range(0, len(n)//2):
        idx = i

        if n[i] != n[-(idx+1)]:
            print("no")
            break
        
        if i == len(n)//2 -1:
            print("yes")
