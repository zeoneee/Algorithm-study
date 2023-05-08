def dfs(visited, v, graph):
    if visited[v] == False:
        visited[v] = True
        print(v,end = ' ')
        network = unleafnode = 0
        for idx,n in enumerate(graph[v]):
            if n == 1 and idx != v and visited[idx] == False:
                unleafnode = 1
                network += dfs(visited, idx, graph)
        return network if unleafnode == 1 else 1  # leafnode인 경우 return 1 
    return 0 # 이미 이전에 방문했던 노드이므로 pass


def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if (dfs(visited,i,computers) != 0):
            answer += 1
    
    return answer