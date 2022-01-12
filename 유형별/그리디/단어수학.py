import sys
import numpy as np

n = int(sys.stdin.readline())
string = []
string_sorted = []
alphabet_num = {}
num = 9

# 단어 입력받기
for _ in range(n):
    string.append(sys.stdin.readline().rstrip())

# 1. 높은 자리에 있는 알파벳이 높은 수
# 2. 같은 자리에 서로 다른 알파벳이 있을 때 더 많이 더해지는 알파벳이 높은 수 

for i in range(n):
    for j in range(len(string[i])):
        if string[i][j] in alphabet_num:
            alphabet_num[string[i][j]] += 10 **(len(string[i])-j-1) # 자릿수 만큼 저장
        else:
            alphabet_num[string[i][j]] = 10 **(len(string[i])-j-1)

for i in alphabet_num.values():
    string_sorted.append(i)

# 자릿수 높은 순으로 정렬
string_sorted.sort(reverse=True)

# 단어의 합 출력 
num_sum = 0
for i in string_sorted: 
    num_sum += num*i
    num -= 1

# 결과 출력 
print(num_sum)

