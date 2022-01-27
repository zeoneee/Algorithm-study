# https://www.acmicpc.net/problem/18406

n = input()
n1, n2 = 0, 0

for i in range(int(len(n)/2)):
    n1 += int(n[i])
for j in range(int(len(n)/2),len(n)):
    n2 += int(n[j])

if n1 == n2:
    print("LUCKY")
else:
    print("READY")

# =================================================================================다른 사람 풀이
# 그냥 sum 함수 이용하는 걸루..

n = list(map(int,input()))
half = len(n)//2

if sum(n[0:half]) == sum(n[half:]):
    print("LUCKY")
else:
    print("READY")