# https://programmers.co.kr/learn/courses/30/lessons/60057
# 완전탐색 알고리즘
# 정답 x

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1): # 1부터 len/2개 단위로 모두 잘라보는 것
        # 전 단계와 cnt 수를 저장할 변수
        short_str = ""
        pre = s[0:i]
        cnt = 1
        # 전 단계와 현재 단계가 동일한 경우
        for j in range(i,len(s),i):
            if pre == s[j:j+i]:
                cnt += 1
        # 전 단계와 현재 단계가 다른 경우
            else:
                if cnt == 1:
                    short_str += pre
                else:
                    short_str += (str(cnt) + pre)
            pre = s[j:j+i] # 초기화
            cnt = 1
        if cnt == 1:
            short_str += pre
        else:
            short_str += (str(cnt) + pre)
        # 최소 문자열 길이
        answer = min(answer,len(short_str))  
    return answer

s = input()
print(solution(s))