T = int(input())
k = 1


for i in range(T):
    testcase = int(input())
    name = []
    for i in range(testcase):
        input_name = input()
        name.append(input_name)

    name = list(set(name))

    name.sort()
    name.sort(key = len)
    testcase = len(name)

    
    
    
        
        
        

        

        
  

    print('#',end='')
    print(k)
    k = k + 1

    for i in range(testcase):
        print(name[i])
    
