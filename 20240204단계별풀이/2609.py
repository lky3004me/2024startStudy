import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().split())
sNum = -1
bNum = -1
gcd = -1
lcm = -1

if n < m:
    bNum = m
    sNum = n
else:
    bNum = n
    sNum = m

#최대공약수
for i in range(sNum, 0, -1):
    if sNum % i ==0 and bNum % i == 0:
        gcd = i
        break

#최소공배수
lcm = int((bNum * sNum)/gcd) 

print(gcd)
print(lcm)