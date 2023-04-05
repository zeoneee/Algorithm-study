import collections

def solution(k, tangerine):
    size = collections.Counter(tangerine)

    total = 0
    for i,v in enumerate(sorted(size.values(), reverse=True)):
        total += v
        if total >= k: return i+1

# collections 모듈의 Counter 함수 사용하여 더 간단하게 해결