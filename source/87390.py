def solution(n, left, right):
    answer = []
    arr = [[0 for j in range(n)] for i in range(n)]
    
    # arr 초기화
    for i in range(n):
        for j in range(i):
            arr[j][i] = i+1
            arr[i][j] = i+1
        arr[i][i] = i+1
    
    # 1차원 배열 만들기
    for a in arr:
        answer += a
    
    answer = answer[left:right+1]
    
    return answer