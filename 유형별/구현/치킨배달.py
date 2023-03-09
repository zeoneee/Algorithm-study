# 완전탐색
from itertools import combinations

n,m = map(int,input().split())
home = []
chicken = []
chicken_m = []

# 집, 치킨집 위치 저장
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(n):
        if li[j] == 1:
            home.append([i,j])
        elif li[j] == 2:
            chicken.append([i,j])


# 치킨집 m개 선택(조합)
for i in combinations(chicken,m):
    chicken_m.append(i)


# 도시의 치킨거리
min_city_chicken = n*n*n
for c_m in chicken_m:     # c는 치킨집 위치의 조합
    sum_city_chicken = 0
    for h in home:
        min_chicken = n*n*n
        for c in c_m:   # 치킨집 조합에서 각 치킨집과 집사이의 치킨거리 
            dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
            if dis < min_chicken:
                min_chicken = dis
        sum_city_chicken += min_chicken
    if sum_city_chicken < min_city_chicken:
        min_city_chicken = sum_city_chicken

print(min_city_chicken)