def solution(babbling):
    says = ["aya","ye","woo","ma"]
    answer = 0
    
    for word in babbling:
        for say in says:
            if say in word and say*2 not in word: # 연속된 say 검사
                word = word.replace(say,"*") # say은 다 *로 바꾸기
                
        if all(char == "*" for char in word):
            answer += 1
        
    return answer