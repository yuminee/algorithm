def solution(numbers):
    a = len(numbers)
    b = 0
    for i in range(0,a):
        for j in range(0,a):
            if (numbers[i] < 10) and (10 <=numbers[j] < 100) :
                if numbers[j]/10 <= numbers[i]:
                    temp = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = temp
                    if numbers[j]%10 > numbers[i]:
                        temp = numbers[j]
                        numbers[j] = numbers[i]
                        numbers[i] = temp
                    if (numbers[j] > numbers[i]) and (numbers[j]%10 ==0):
                        temp = numbers[j]
                        numbers[j] = numbers[i]
                        numbers[i] = temp
                if numbers[i] == 1000:
                    temp = numbers[a-1]
                    numbers[a-1] = numbers[i]
                    numbers[i] = temp
                if numbers[i] ==0:
                    b = b + 1


            
    
    
    y = ''

    for i in range(0,a):
        x = str(numbers[i])
        y = y+x
    
    for i in range(0,b):
        y = y+'0'    
    return y
