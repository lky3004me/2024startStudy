import sys

sys.stdin = open("input.txt", "r")
s, p = map(int, sys.stdin.readline().split())
dna = list(sys.stdin.readline())
restrain = list(map(int, sys.stdin.readline().split()))
cnt = [0]*4
rst = 0

start = 0
end = p-1
for i in range(s-p+1):
    for j in range(p):
        if dna[start+j] == 'A':
            cnt[0] +=1
        elif dna[start+j] == 'C':
            cnt[1] +=1
        elif dna[start+j] == 'G':
            cnt[2] +=1
        elif dna[start+j] == 'T':
            cnt[3] +=1

    if cnt[0] >= restrain[0] and cnt[1] >= restrain[1] and cnt[2] >= restrain[2] and cnt[3] >= restrain[3]:
        rst +=1        
    cnt = [0]*4
    start +=1
    end +=1
    
print(rst)
        
