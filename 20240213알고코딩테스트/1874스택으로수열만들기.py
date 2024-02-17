import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
stack = []
rst = ""
result = True
num =1

for i in range(n):
    input = int(sys.stdin.readline())
    
    if input >= num:
        while input >= num:
            stack.append(num)
            num +=1
            rst += "+\n"
        stack.pop()
        rst += "-\n"
    else:
        tmp = stack.pop()
        if tmp > input:
            print("NO")
            result = False
            break
        else:
            rst += "-\n"
        
if result:
    print(rst)

    
        
    
    

