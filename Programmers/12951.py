def solution(s):
    answer = ''
    jadencase = s.split(" ")
    print(jadencase)
    for j in jadencase:
        if j == '':
            answer += " "
        elif j[0].isdigit():
            answer += j.lower() + ' '
        else:
            temp = j[0].upper()
            temp += j[1:].lower()
            answer += temp + ' '
    
    return answer[:-1] # 마지막 띄어쓰기 제외