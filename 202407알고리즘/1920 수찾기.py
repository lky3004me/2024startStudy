import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")

n = int(input())
origin = sorted(list(map(int, input().split())))  # 이진 탐색을 위해 정렬

m = int(input())
target = list(map(int, input().split()))


#그냥 비교는 안 됨 10의 6승이라, 그냥 1초 초과됨.
#이진 탐색 구현 필요
# 이진 탐색은 가운데를 지정, 
#5 2 1


def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return 0  

for i in range(len(target)):
    print(binary_search(origin, target[i]))