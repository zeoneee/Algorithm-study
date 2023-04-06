def solution(name, yearning, photo):
    answer = []
    miss = {}
    
    # 그리움 점수 매핑하기
    for i,v in enumerate(name):
        miss[v] = yearning[i]
        
    # 그리움 더하기
    for p in photo:
        misspoint = 0
        for name in p:
            if name in miss:
                misspoint += miss[name]
        answer.append(misspoint)
    
    return answer
