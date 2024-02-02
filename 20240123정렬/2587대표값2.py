import sys

sys.stdin = open("input.txt", "r")
arr = []
for _ in range(5):
    arr.append(int(sys.stdin.readline()))

n = len(arr)
for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

middle = n//2
sum = 0
for element in arr:
    sum += element
rst = sum //n

print(rst)
print(arr[middle])
