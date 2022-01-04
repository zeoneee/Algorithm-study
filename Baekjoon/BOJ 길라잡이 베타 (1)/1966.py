import sys
from sys import stdin

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    n,m = list(map(int,input().split()))
    num = list(map(int,input().split()))

    test = num[m]
    num.sort(reverse=True)

    print(num.index(test)+1)



