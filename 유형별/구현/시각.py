n = int(input())
h,m,s = 0,0,0
cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)