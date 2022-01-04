m,n = map(int,input().split())

li = [False,False]+[True]*(n-1) 

for i in range(2,n+1):
    if li[i] :
        if i >= m:
            print(i)
        for j in range(i+i,n+1,i):
            li[j] = False

# prime list 만들어서 다시 재 출력하는거 없이 
# 바로 소수 검사해서 출력했더니 시간 초과 x