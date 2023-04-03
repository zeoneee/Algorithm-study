# 1차원 배열 줄 세워서 인덱스랑 값 비교해보기

def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        x = idx // n
        y = idx % n
        answer.append(max(x,y)+1)
    return answer