# dfs
def solution(begin, target, words):
    stack = [(begin,0)] #현재 word, depth
    while stack:
        temp, cnt = stack.pop(0)
        if temp == target:
            return cnt
        for idx,word in enumerate(words):
            if sum(i!=j for i,j in zip(temp,word)) == 1:
                del words[idx]
                print(word,cnt)
                stack.append((word,cnt+1))
    return 0

# 규진 코드: stack에 visit 해야할 tuple들을 넣은 후 visit 할 때마다 pop. 
# depth는 cnt 변수를 이용하여 계산함. 
# stack.pop(0)을 하는 이유는 depth 계산을 중복해서 하지 않기 위해 
#   → 더 자세하게 숙지하기