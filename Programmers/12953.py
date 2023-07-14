# 최대 공약수의 배수 
def solution(arr):
    answer = 0
    gcd = 0
    # 최대공약수 찾기
    for i in range(2,max(arr)+1):
        ck = True
        for j in arr:
            if j%i != 0:
                ck = False
                break
        if ck == False:
            break
        else:
            gcd = i
            break
    
    # 최소공배수 찾기
    if gcd == 0:
        answer = 1
        for i in arr:
            answer *= i
        return answer
    else:
        while True:
            for i in range(gcd,100000000,gcd):
                ck = True
                for j in arr:
                    if i%j != 0:
                        ck = False
                        break
                if ck == True:
                    return i