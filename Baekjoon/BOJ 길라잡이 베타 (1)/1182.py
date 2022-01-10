from itertools import combinations

n,s = list(map(int,input().split()))
num = list(map(int,input().split()))
test = []

cnt = 0
for i in range(1,n+1): # i = 부분수열 원소의 개수 (1부터 원소개수 조합까지) 
    test = list(combinations(num,i)) # test의 개수 
    for tc in range(len(test)): 
        sum = 0
        for j in range(i):
            sum+=test[tc][j]
        if sum == s:
            cnt+=1
print(cnt)

# 부분수열 구하기 -> 원소의 합 구하기 -> s면 cnt++
# 모든 부분수열의 합 보기 

# sum도 내장함수가 있구나........
# n,s = map(int,input().split())
