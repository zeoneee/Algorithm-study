import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())

words_s = set(words)  # 중복 제거
words_l = list(words_s) 

words_l.sort()
words_l.sort(key=len)

for i in words_l:
    print(i)