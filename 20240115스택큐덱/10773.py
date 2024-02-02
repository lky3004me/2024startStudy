K = int(input())
myStack = []

for i in range(K):
    num = int(input())

    if num == 0:
        myStack.pop()
    else:
        myStack.append(num)
    
print(sum(myStack))