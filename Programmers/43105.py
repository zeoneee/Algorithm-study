def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for x in range(1,n):    # 각 자릿수마다 dp에 최종합 더해줌
        for y in range(len(triangle[x])):
            if y==0:
                dp[x][y] = triangle[x][0] + dp[x-1][0]
            elif x==y:
                dp[x][y] = triangle[x][0] + dp[x-1][y-1]
            else:
                dp[x][y] = max(triangle[x][y] + dp[x-1][y-1], triangle[x][y] + dp[x-1][y])

    answer = max(dp[-1])
    return answer