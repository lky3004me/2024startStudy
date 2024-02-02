import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
target = []

for _ in range(n):
    target.append(int(sys.stdin.readline()))

def bubble(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
def select(arr):
    n = len(arr)
    for i in range(0, n-1):
        mIdx = i
        for j in range(i+1, n):
            if arr[mIdx] > arr[j]:
                mIdx = j
        arr[i], arr[mIdx] = arr[mIdx], arr[i]

def insert(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2
        



bubble(target)
#select(target)
#insert(target)
for element in target:
    print(element)
