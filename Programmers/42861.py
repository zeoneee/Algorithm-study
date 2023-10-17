def solution(n, costs):
    answer = 0
    
    # union & find 자료구조
    parents = [i for i in range(n)]
    
    def find(n): # 최상위 노드 찾기
        if parents[n] == n:
            return n
        return find(parents[n])
        
    def union(a,b):
        a = find(a)
        b = find(b)
    
        if a != b:
            parents[a] = b # 서로 다른 두 집합 노드 합치기(루트 노드를 합치면서)
            
    # 최소신장트리
    costs.sort(key=lambda x:x[2])
    for a,b,c in costs:
        # 두 노드가 같은 부모를 가졌는지 확인, 가지지 않았다면 서로소 집합
        if find(a) != find(b):
            union(a,b)
            answer += c
    
    return answer