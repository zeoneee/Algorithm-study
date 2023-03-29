def solution(clothes):
    answer = 1
    closet = {}
    
    for c in clothes:
        if c[1] in closet:
            closet[c[1]].append((c[1],c[0]))
        else:
            closet[c[1]] = [(c[1],c[0])]
    
    for v in closet.values():
        answer *= (len(v)+1)
        
    answer -= 1
    
    return answer

    # append list하던지 tuple하던지 상관없음