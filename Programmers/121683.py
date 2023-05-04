def solution(input_string):
    answer = ''
    temp_list = []
    i = 0
    for a in input_string:
        if a in temp_list:
            temp = temp_list.pop()  # 직전 index value pop
            if temp != a: 
                if not(a in answer):
                    answer += a
            temp_list.append(temp)
            temp_list.append(a)
            i += 1
        else:
            temp_list.append(a)
            i += 1
            
    answer = ''.join(sorted(list(answer)))
    
    if answer == "":
        answer = "N"
        
    return answer