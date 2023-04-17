# deque 이용한 풀이
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()   
    pp = deque(people)
    
    while len(pp) > 1:
        if pp[0]+pp[-1] <= limit: 
            pp.popleft()
        pp.pop() # 위 조건을 만족하던지 말던지 end값은 pop
        answer += 1
    if pp: # 1만 남아있을 수도 있으니까
        answer += 1

    return answer