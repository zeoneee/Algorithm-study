def solution(citations):
    answer = 0
    citation_dict = {}
    
    # dictionary에 citations의 max값 까지 인용횟수 할당하기
    for i in range(max(citations) + 1):
        if i in citations:
            citation_dict[i] = citations.count(i)
        else:
            citation_dict[i] = 0
            
    # dictionary 정렬 후 검사
    citation_dict = dict(sorted(citation_dict.items(),reverse=True))

    # i 이상 value값의 합이 i이상이면 return
    for i in citation_dict:
        sum_of_values = 0
        for key, value in citation_dict.items():
            if key >= i:
                sum_of_values += value
            
        if sum_of_values > i:
            return i+1
    
    return answer
