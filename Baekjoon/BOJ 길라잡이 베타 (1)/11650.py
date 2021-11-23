import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1])
arr.sort()

for i in arr:
    print(i[0],i[1])

# 먼저 y기준
# 그다음 x기준 