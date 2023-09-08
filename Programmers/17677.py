# J(A,B) = 두 집합의 교집합 크기 / 두 집합의 합집합 크기
import re

def solution(str1, str2):    
    answer = 0
    
    # 다중집합 만들기
    s1, s2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i].upper()+str1[i+1].upper())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i].upper()+str2[i+1].upper())   
        
    print(s1,s2)
    
    if len(set(s1)&set(s2)) == 0 or len(set(s1+s2)) == 0:
        return 65536
    answer = (len(set(s1)&set(s2))/len(set(s1+s2))) * 65536
    return answer

# 같은 문자도 다르게 판단해야하나봄 그럼 set을 사용하면 안되는데