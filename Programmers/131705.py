from itertools import combinations
def solution(number):
    answer = 0
    for s in combinations(number,3):
        if sum(s) == 0:
            answer += 1
    return answer