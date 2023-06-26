def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    for i in range(l):
        if k >= max(dungeons)[0]:
            dungeons.sort(key=lambda x:x[1])
            k -= dungeons.pop(0)[1]
            answer += 1
        else:
            dungeons.remove(max(dungeons))
    return answer

# k보다 최소피로도가 작은 애들 중에 소모피로도가 적은 순으로 