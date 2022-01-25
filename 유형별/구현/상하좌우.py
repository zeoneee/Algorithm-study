import sys

n = int(sys.stdin.readline())
plan = list(map(str,input().split()))   # input().split() 하면 됨
destination = [1,1] # x,y = 1,1 로 놓고 하는게 더 나음 괜히 list 추가하지말고 

for i in range(len(plan)):
    if plan[i] == 'L':
        if destination[1] != 1:
            destination[1] -= 1
    elif plan[i] == 'R':
        if destination[1] != n:
            destination[1] += 1
    elif plan[i] == 'U':
        if destination[0] != 1:
            destination[0] -= 1
    elif plan[i] == 'D':
        if destination[0] != n:
            destination[0] += 1

print(destination[0],destination[1])