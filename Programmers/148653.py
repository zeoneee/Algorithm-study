def solution(storey):
    answer = 0
    storey = list(map(int,str(storey)))
    if storey[-1] >= 5:
        answer = sum(storey[:-1]) + 1 + 10-storey[-1]
    else:
        answer = sum(storey)
    return answer