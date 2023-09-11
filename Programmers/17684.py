# A:65
def solution(msg):
    answer = []
    alpha = {}
    cnt = 27
    
    # 사전 만들기
    for i in range(65,91):
        alpha[chr(i)] = i-64
    
    i = 0
    while i < len(msg):
        
        # 가장 긴 문자열 
        j = len(msg)
        while j >= i:
            if msg[i:j] not in alpha:
                j -= 1
            else:
                break
        
        answer.append(alpha[msg[i:j]])
        alpha[msg[i:j+1]] = cnt
        cnt+=1
        i = j
            
    return answer