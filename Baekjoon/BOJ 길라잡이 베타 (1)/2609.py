"""
    런타임 에러
    1. zerodivisionerror: 0으로 나누었을 때 발생
    2. IndexError: 인덱싱 할 때 길이 초과
    3. NameError: 선언하지 않은 변수 사용했을 때 
"""

def div(n1,n2):
    for i in range(min(n1,n2),0,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return -1

def mul(n1,n2):
    n = div(n1,n2) 
    print(n) # 최대공약수 출력 

    for i in range(max(n1,n2),n1*n2+1,n):
        if i % n1 == 0 and i % n2 == 0:
            return i
    return -1

n1, n2 = map(int,input().split())
print(mul(n1,n2))

# n1 or n2가 1인 경우 index에러 조심 
# 1도 최대공약수 ..
