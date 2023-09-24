#내 행과 다음 행을 비교했을 때 
def solution(land):
    answer = 0
    
    for i in range(len(land)):
        if i+1 == len(land):
            answer += max(land[i])
        elif land[i].index(max(land[i])) != land[i+1].index(max(land[i+1])):
            answer += max(land[i])
        else:
            temp_i = land[i].copy()
            temp_i.remove(max(land[i]))
            temp_i1 = land[i+1].copy()
            temp_i1.remove(max(land[i+1]))
            if max(land[i]) + max(temp_i1) > max(temp_i) + max(land[i+1]):
                answer += max(land[i])
                land[i+1] = temp_i1
            else:
                answer += max(temp_i)
    return answer