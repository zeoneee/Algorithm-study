def solution(n, m, section):
    answer = 1
    
    temp = section[0]
    for s in section:
        if s > temp+m-1:
            answer += 1
            temp = s    # index 다음 위치로 갱신
    
    return answer

    # 생각보다 간단한 문제