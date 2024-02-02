import sys
sys.stdin = open("input.txt", "r")

while(True):
    myStack = []
    str = input()

    if str == '.':
        break

    for ch in str:
        if ch in ["(", "["]:
            myStack.append(ch)
        
        elif ch == ')':
            if myStack and myStack[-1] == '(':
                myStack.pop()
            else:
                myStack.append(')')
        elif ch == ']':
            if myStack and myStack[-1] == '[':
                myStack.pop()
            else:
                myStack.append(']')

        
    
    if len(myStack) == 0:
        print('yes')
    else:
        print('no')

 