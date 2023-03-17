# 시간초과

# BST
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self,head):
        self.head = head    # 부모노드
    
    def insert(self,value):
        self.base = self.head
        while True:
            if self.base.value > value:   # 삽입값이 좌측노드에
                if self.base.left != None:
                    self.base = self.base.left
                else : 
                    self.base.left = Node(value)
                    break
            else : # 삽입값이 우측노드에
                if self.base.right != None:
                    self.base = self.base.right
                else:
                    self.base.right = Node(value)
                    break
    
    def search(self,value):
        self.base = self.head
        
        while self.base:
            if self.base.value == value:    # 이 경우는 없다고 가정. 
                return self.base.value
                break
                
            elif self.base.value > value:
                if self.base.left != None:
                    self.base = self.base.left
                else: # 좌측 노드 없음
                    return self.base.value, 0   # 0: 해당 값 사용
            
            elif self.base.value < value:
                if self.base.right != None:
                    self.base = self.base.right
                else: # 우측 노드 없음
                    return self.base.value, 1


def solution(n, m, section):
    answer = 0
    section_temp = section.copy()
    h = section_temp.pop(len(section_temp)//2)
    
    # bst 생성
    head = Node(h)
    bst = BST(head) 
    for num in section_temp:
        bst.insert(num)
        
    i = 0
    while i < len(section):
        if section[i] + m in section:
            i = section.index(section[i]+m)
            answer += 1
        else:
            node, loc = bst.search(section[i]+m)
            print(node)
            if loc == 0:
                i = section.index(node)
                answer += 1
            else:
                i = section.index(node) + 1
                answer += 1
    
    return answer

def main():
    n = 5	
    m = 4
    section = [1,3]
    
    print(solution(n,m,section))
    
    return

if __name__ == '__main__':
    main()