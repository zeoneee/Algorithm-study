x = int(input())

dp = [0]*30001

for i in range(2,x+1):
    dp[i] = dp[i-1] + 1 # x-1
    print()
    print(i,dp[i],": ", end='')
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
        print(dp[i], end=' ')
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
        print(dp[i], end=' ')
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
        print(dp[i], end=' ')

print()
print("answer: ",dp[x])