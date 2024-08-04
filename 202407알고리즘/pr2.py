import sys
sys.stdin = open("input.txt" , "r")

N, M = map(int, input().split())
h = list(map(int, input().split()))
graph = [[0 for _ in range(N)]for _ in range(M)]

	
#N은 가로길이
for i in range(N):
	for num in h:
		if num >= 0:
			for j in range(M-1, M-1-num,-1):
				graph[j][i] =1
					
		else:
			for j in range(0, abs(num)):
				graph[j][i] = 1
				
		break
            

print(graph)
			