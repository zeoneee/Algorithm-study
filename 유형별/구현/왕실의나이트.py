# 완전탐색(brute forcing)

# 위치 입력받기 
location = input()
alpa = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
x = alpa[location[0]] # alpa[location[0]] : 숫자 
y = int(location[1])

# 방향 설정
direction = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]

cnt = 0
for i in range(8): # 8방향 검색
    dx = x + direction[i][0]
    dy = y + direction[i][1]
    # 해당 위치로 이동가능하면 카운트 증가
    if 1 <= dx <= 8 and 1 <= dy <= 8:
        cnt += 1

print(cnt)

