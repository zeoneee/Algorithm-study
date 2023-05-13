def solution(storey):
    answer = 0
    storey = list(map(int,str(storey)))
    for i,s in enumerate(storey):
        if s > 5:
            if i != len(storey)-1:
                if storey[i+1] >5:
                    answer += 10-s-1
                else:
                    answer += 10-s
            else:
                answer += 10-s
        else:
            if i != len(storey)-1:
                if storey[i+1] >5:
                    answer += s+1
                else:
                    answer += s
            else:
                answer += s
                
    return answer