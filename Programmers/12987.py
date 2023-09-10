def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(A)):
        temp = B.pop()
        if A[i] < temp:
            answer += 1
        else:
            B.append(temp)
        
    return answer