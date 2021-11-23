import sys

n = int(sys.stdin.readline())
num = []
arr = []
num.append(list(map(int,input().split())))

for i in range(n):
    arr.append(num[0][i])

arr = set(arr)  # 중복 제거
arr = list(arr) 
arr.sort()

for i in arr:
    print(i,end=" ")