import math

def solution(brown, yellow):
    answer = []
    
    # x**2 - (brown+4)/2x + (brown+yellow) = 0
    # 근의 공식
    
    x = ((brown+4)/2+math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    answer.append(x)
    answer.append((brown+yellow)/x)
    
    return answer