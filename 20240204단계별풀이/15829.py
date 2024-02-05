import sys
sys.stdin = open("input.txt", "r")

L = int(sys.stdin.readline())
r = 31
M = 1234567891
sum = 0
str = sys.stdin.readline().strip()

for i in range(L):
    a = int(ord(str[i])) - 96 
    sum += a * r**i

H = sum % M

print(H)