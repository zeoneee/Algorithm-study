def solution(babbling):
    answer = 0
    for word in babbling:
        i = 0
        while i < len(word):
            if word[i:i+3] == "aya":
                i += 3
            elif word[i:i+2] == "ye":
                i += 2
            elif word[i:i+3] == "woo":
                i += 3
            elif word[i:i+2] == "ma":
                i += 2
            else:
                print(word)
                answer -= 1
                break
        answer += 1
    return answer