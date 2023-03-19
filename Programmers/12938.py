def solution(n, s):
    q = s//n
    r = s%n
    
    if q == 0:
        return [-1]
    else:
        answer = [q for i in range(n)]
        for i in range(r):
            answer[i] += 1
        answer.sort()
        
        return answer