# push, pop, size, empty, top

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        num = command[1]
        stack.append(num)
    
    elif command[0] == "pop":
        if len(stack)==-0:
            print(-1)
        else:
            print(stack.pop())
    
    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if len(stack)==0:
            print(1)
        else: print(0)

    elif command[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
