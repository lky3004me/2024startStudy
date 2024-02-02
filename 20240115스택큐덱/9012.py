T = int(input())

for _ in range(T):
    myStack = []
    isVPS = True
    str = input()

    for ch in str:
        if ch == '(':
            myStack.append(ch)
        if ch == ')':
            if myStack:
                myStack.pop()
            elif not myStack:
                isVPS = False
                break
        
    if not myStack and isVPS:
        print('YES')
    elif myStack or not isVPS:
        print('NO')
    