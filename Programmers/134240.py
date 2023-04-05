def solution(food):
    answer = ''
    
    for i, v in enumerate(food[1:]):
        answer += str(i+1)*(v//2)
    
    return answer + '0' + answer[::-1]

# 기존 코드보다 더 간단하게 solved