import sys

n = int(sys.stdin.readline())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
sum = 0
for i in range(n):
  sum += a[i]*b.pop(b.index(max(b)))  

print(sum)


