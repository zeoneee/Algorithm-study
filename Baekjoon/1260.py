# 입력을 graph 형식으로 받으면 바로 넣으면 됨
# edge형태로 넣으면 graph로 변환해야함. 

from collections import deque

def dfs(graph, v, visited):
    if visited[v] == False:
        # 현재 노드 방문처리
        visited[v] = True
        print(v, end=' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]: # graph[v]가 [v]랑 연결된 다른 노드들 
            dfs(graph, i, visited)


queue = deque()

def bfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        print(v, end=' ')
    
        for i in graph[v]:              # 이웃 노드를 다 넣어주는게 핵심
            if visited[i] == False:     # 불필요한 탐색 횟수 제거하기 
                queue.append(i)
    
    if len(queue) > 0:
        bfs(graph, queue.popleft(), visited)

def main():
    n,m,v = map(int,input().split())
    visited_d = [False]*(n+1)
    visited_b = [False]*(n+1)
    graph_d = [[] for _ in range(n+1)] 
    graph_b = [[] for _ in range(n+1)] 

    for _ in range(m):
        a,b = map(int,input().split())
        graph_d[a].append(b)
        graph_d[b].append(a)
        graph_b[a].append(b)
        graph_b[b].append(a)

    dfs(graph_d, v, visited_d)
    print()
    bfs(graph_b, v, visited_b)


if __name__ == "__main__":
    main()
 


