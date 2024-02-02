import sys
sys.stdin = open("input.txt", "r")
arr = sys.stdin.readline()
time = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for ele in arr:
    for i in dial:
        if ele in i:
            time += dial.index(i)+3
print(time)