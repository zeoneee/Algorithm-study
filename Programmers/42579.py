def solution(genres, plays):
    
    answer = []
    genres_plays = {}
    index_plays = {}

    # 장르별 재생횟수, 인덱스별 재생횟수
    for i in range(len(genres)):
        if genres[i] in genres_plays:
            genres_plays[genres[i]] += plays[i]
            index_plays[genres[i]].append((i,plays[i]))
        else:
            genres_plays[genres[i]] = plays[i]
            index_plays[genres[i]] = [(i,plays[i])]
            
    # 속한 노래가 많이 재생된 장르 찾기
    genres_plays = dict(sorted(genres_plays.items(), key=lambda x:x[1], reverse=True))
    
    for g in genres_plays:
        index_plays[g] = sorted(index_plays[g], key=lambda x:x[1], reverse=True)
    
        
        if len(index_plays[g]) == 1:
            answer.append(index_plays[g][0][0])
        else:
            answer.append(index_plays[g][0][0])
            answer.append(index_plays[g][1][0])
        
                                   
    return answer