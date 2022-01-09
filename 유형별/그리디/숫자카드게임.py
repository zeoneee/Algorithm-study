import numpy as np

n,m = map(int,input().split())
data = np.zeros((n,m))

# data 입력
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(m):
        data[i][j]=li[j]

# 각 행에서 min값 뽑아서 그 중 가장 큰 값 출력
check=[]
for i in range(n):
    check.append(min(data[i]))
check.sort(reverse=True)
print(int(check[0]))

"""===================================answer==================================="""

# 행에 따라 데이터 입력받고 바로 min값 select
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)



