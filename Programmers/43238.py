def solution(n, times):
    answer = 0
    l,r = 1, max(times)*n # r은 최악의 상황
    
    while l <= r:
        m = (l+r)//2 
        people = 0 # peple = m분 동안 심사한 사람의 수
        
        for time in times:
            people += m//time
            if people >= n:
                break
        
        if people >= n: # 시간 충분 =>  줄임
            answer = m
            r = m - 1
        elif people < n: # 시간 부족 => 줄임
            l = m + 1
                
    return answer