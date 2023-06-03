def solution(n):
    answer = 0
    for i in range(1,n+1):
        cnt = 0; j = i
        while cnt < n:
            cnt += j
            j += 1
        if cnt == n:
            answer += 1
    return answer