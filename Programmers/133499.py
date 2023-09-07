def solution(babbling):
    answer = 0
    for word in babbling:
        i = 0
        prev = ""
        while i < len(word):
            if word[i:i+3] == "aya":
                if prev == "aya":
                    answer -= 1
                    break
                prev = "aya"
                i += 3
            elif word[i:i+2] == "ye":
                if prev == "ye":
                    answer -= 1
                    break
                prev = "ye"
                i += 2
            elif word[i:i+3] == "woo":
                if prev == "woo":
                    answer -= 1
                    break
                prev = "woo"
                i += 3
            elif word[i:i+2] == "ma":
                if prev == "ma":
                    answer -= 1
                    break
                prev = "ma"
                i += 2
            else:
                answer -= 1
                break
        answer += 1
    return answer