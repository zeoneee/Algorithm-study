def solution(numbers):
    numbers = list(map(str, numbers)) # 리스트의 모든 요소를 문자열로 변환
    numbers.sort(key=lambda x: x*3, reverse=True) # 문자열을 3번 반복하여 비교하여 정렬
    return str(int(''.join(numbers))) # 리스트를 문자열로 결합하여 정수로 변환 후 다시 문자열로 반환