def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    
    for i in range(l):
        for j in range(l-1,-1,-1):
            if i !=j:
                so = len(phone_book[i])
                compare = phone_book[j]
                spilt_compare = compare[0:so]
                
                if phone_book[i] == spilt_compare:
                    return False
    
    return True
