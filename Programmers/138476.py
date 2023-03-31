def solution(k, tangerine):
    answer = 0
    t_size = [0]*max(tangerine)
    
    for t in tangerine:
        t_size[t-1] += 1
    
    t_size.sort(reverse=True)
    
    tangerines = 0
    for s in t_size:
        if tangerines < k:
            tangerines += s
            answer += 1
        else:
            break
    
    return answer


