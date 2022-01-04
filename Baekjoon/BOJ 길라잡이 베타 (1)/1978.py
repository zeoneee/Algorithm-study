# 에라토스테네스의 체 
import sys

li = [i for i in range(2,1001)] 
for i in range(1,len(li)-1):
    # 앞에서 부터 차례대로
    for j in range(i+1,len(li)):
        if li[i] == -1:
            break
        else:
            if li[j] % li[i] == 0:
                # 해당 숫자의 배수는 list에서 삭제
                li[j] = -1  

def issosu(n):
    if n in li:
        return True
    else:
        return False

n = int(sys.stdin.readline())
num = list(map(int,input().split()))
cnt = 0

for i in range(n):
    if issosu(num[i]):
        cnt += 1

print(cnt) 

