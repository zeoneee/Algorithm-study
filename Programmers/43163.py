# bfs
# 처음에 bfs로 시작해서 품. -> 애초에 깊이탐색이라 bfs가 아니라 dfs문제인듯
# 탐색값이 hit→hot→dot→lot→dog→log→cog 값으로 예상했던 탐색 순서는 맞는데 level을 안따지고 pop할때마다 cnt값 늘려줘서 탐색할때마다 값이 늘어남. 
# level을 고려해야하는데 아직 못짬

from collections import deque

def solution(begin, target, words):
    answer = cnt = 0
    if not(target in words):
        return answer
    
    def checkTwo(w1,w2): # 두 개 이상의 알파벳이 같은지 비교
        cnt = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                cnt += 1
        return True if cnt >= 2 else False
    
    def bfs(begin, cnt):
        queue = deque()
        queue.append(begin)
        visited = [False]*len(words)
        
        while queue:
            word = queue.popleft()
            print(word)
            if word == target:
                return cnt
            else:
                for i,w in enumerate(words):        
                    if visited[i] == True:
                        continue
                    else:
                        if checkTwo(word,w):
                            cnt += 1
                            visited[i] = True
                            queue.append(w)
                
    return bfs(begin,cnt)