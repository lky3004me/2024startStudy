import sys

s = list(input().strip())
t = list(input().strip())

switch = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
    if s == t:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)