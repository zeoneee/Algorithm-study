import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    if sum(works) < n: # 야근이 없는 경우
        return answer
    
    for w in works: # 최대 힙 만들기
        heapq.heappush(heap, -w)
    for _ in range(n):
        heapq.heappush(heap,heapq.heappop(heap)+1)
    while heap:
        answer += heapq.heappop(heap)**2
        
    return answer