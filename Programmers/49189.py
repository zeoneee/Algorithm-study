def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1]*(n+1)
    
    # 각 노드가 연결된 정보를 표현
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    stack = [1]
    distance[1] = 0
    
    while stack:
        now = stack.pop(0)
        for i in graph[now]:
            if distance[i] == -1:
                stack.append(i)
                distance[i] = distance[now] + 1 # 최단거리 갱신
    
    maxv = max(distance)
    for d in distance:
        if d == maxv:
            answer += 1
    
    return answer