def solution(s):
    answer = ''
    jadencase = s.split()
    for j in jadencase:
        if j[0].isdigit():
            answer += j.lower() + ' '
        elif j[0] == ' ':
            answer += j[0]
        else:
            temp = j[0].upper()
            temp += j[1:].lower()
            answer += temp + ' '
    
    return answer[:-1] # 마지막 띄어쓰기 제외
    