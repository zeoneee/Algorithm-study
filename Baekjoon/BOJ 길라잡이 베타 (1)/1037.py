import sys

n = int(sys.stdin.readline())
div = list(map(int,input().split()))

div.sort()
print(div[0]*div[n-1])

