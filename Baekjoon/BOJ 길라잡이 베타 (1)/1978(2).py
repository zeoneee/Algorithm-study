import sys

n = int(sys.stdin.readline())
num = list(map(int,input().split()))
cnt = 0

for i in range(n):
    check = 0
    if num[i] == 1:
        continue
    else:   
        for j in range(2,num[i]):
            if num[i] % j == 0:
                check = 1
                break
        if check == 0:
            cnt += 1
print(cnt)

# 2부터 n까지 n을 i로 나눴을 때 나머지가 0인 수가 하나도 없다면 소수