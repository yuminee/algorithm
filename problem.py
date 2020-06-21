
number = 1
for a in range(10):
    number_Of_view = 0
    
    number_Of_Building = int(input())

    list_Of_Building=[int(x) for x in input().split()]
    


    for i in range(2,number_Of_Building-2):
        if (list_Of_Building[i] > list_Of_Building[i-1]) and (list_Of_Building[i] > list_Of_Building[i-2]):
            if (list_Of_Building[i] > list_Of_Building[i+1]) and (list_Of_Building[i] > list_Of_Building[i+2]):
                tem_list = []
                tem_list.append(list_Of_Building[i-2])
                tem_list.append(list_Of_Building[i-1])
                tem_list.append(list_Of_Building[i+1])
                tem_list.append(list_Of_Building[i+2])
                tem_list.sort(reverse=True)
                number_Of_view = number_Of_view +(list_Of_Building[i] - tem_list[0])
                
                
            
            

    print('#',end='')
    print(number, end=' ')
    print(number_Of_view)
    number = number +1 
