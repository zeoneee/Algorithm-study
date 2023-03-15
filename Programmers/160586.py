from string import ascii_uppercase

def solution(keymap, targets):
    answer = []
    
    alphabet_dict = {}                      
    for i in ascii_uppercase:
	    alphabet_dict[i] = -1
    
    # 문자별 최소 눌러야 하는 횟수
    for alpha in alphabet_dict.keys():
        # 각 alpha에 대해 
        min_idx = 999
        for key in keymap:
            for i in range(len(key)):
                if key[i] == alpha:
                    if i+1 < min_idx:
                        min_idx = i+1
                    break
            if min_idx == 1:
                break
        if min_idx == 999:
            continue
        alphabet_dict[alpha] = min_idx
    
    # 최소 입력 횟수 더하기
    end = False
    for target in targets:
        min_push = 0
        for char in target:
            if alphabet_dict[char] == -1:
                answer.append(-1)
                end = True 
                break   # 해당 target이 -1일 경우
            else:
                min_push += alphabet_dict[char]
        if end == True: # 해당 target이 -1일 경우 
            end = False
            continue
        answer.append(min_push)
                
        
    return answer