def solution(word):
    start = ["A","E","I","O","U"]
    words = []
    for a in range(5):
        words.append(start[a])
        for b in range(5):
            words.append(start[a]+start[b])
            for c in range(5):
                words.append(start[a]+start[b]+start[c])
                for d in range(5):
                    words.append(start[a]+start[b]+start[c]+start[d])
                    for e in range(5):
                        words.append(start[a]+start[b]+start[c]+start[d]+start[e])
    
    answer = words.index(word)+1
    return answer