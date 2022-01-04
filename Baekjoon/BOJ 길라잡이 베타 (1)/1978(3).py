import sys

nc = 1000
li = [False,False]+[True]*(nc-1) # 0까지 포함해서 1000000+1개
primes = []

for i in range(2,nc+1):
    if li[i]:
        primes.append(i)
        for j in range(i+i,nc+1,i):
            li[j] = False

n = int(sys.stdin.readline())
num = list(map(int,input().split()))
cnt = 0

for i in range(n):
    if num[i] in primes:
        cnt += 1
print(cnt)
