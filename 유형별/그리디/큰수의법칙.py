n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort(reverse=True)

# k번 num[0]더하고, 한 번 num[1]더하고 .. m번까지 
Sum = 0
cnt = 0
for _ in range(m):
    if cnt == k:
        Sum += num[1]
        cnt = 0
        continue
    Sum += num[0]
    cnt += 1
    
print(Sum)
