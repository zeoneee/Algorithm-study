# 유사도: 교집합 / 합집합
# 다중집합 개념 사용

def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            s1.append(str1[i:i+2].upper())
            
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            s2.append(str2[i:i+2].upper())
            
    # 다중집합의 합집합
    s1_temp = s1.copy()
    s1_result = s1.copy() # 합집합
    
    for s in s2:
        if s in s1_temp:
            s1_temp.remove(s)
        else:
            s1_result.append(s)
    
    # 다중집합의 교집합
    s1_result2 = []
    for s in s2:
        if s in s1:
            s1.remove(s)
            s1_result2.append(s)
        
    if len(s1_result) == 0 and len(s1_result2) == 0:
        answer = 1
    else:
        answer = len(s1_result2)/len(s1_result)
        
    return int(answer*65536)