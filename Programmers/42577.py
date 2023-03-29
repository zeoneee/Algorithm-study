def solution(phone_book):
    answer = True
    phone_book.sort() 
            
    for i, phone in enumerate(phone_book):
        if i != len(phone_book) -1:
            if phone == str(phone_book[i+1])[0:len(phone)]:
                    return False
    
    return answer