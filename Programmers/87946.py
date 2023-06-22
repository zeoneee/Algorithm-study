def solution(k, dungeons):
    answer = 0
    while len(dungeons) > 0:
        dungeons.sort(reverse=True)
        l = len(dungeons)
        for i in range(l): # 0,1,2
            if k >= dungeons[i][0]:
                temp_dungeons = dungeons[i:]
                temp_dungeons.sort(key=lambda x:x[1])
                k -= temp_dungeons.pop(0)[1]
                answer += 1
        dungeons = temp_dungeons
    return answer

# k보다 최소피로도가 작은 애들 중에 소모피로도가 적은 순으로 