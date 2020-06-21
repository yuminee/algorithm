num = int(input()) 
k =1

for k in range(0,num):
    size = int(input())
    halfsize = int(size/2)
    get = 0
    origin_harvest = [list(map(int, input())) for _ in range(size)]
    
    

    for i in range(0, halfsize):
        for j in range(halfsize-i, halfsize+i+1):
            get += origin_harvest[i][j]

    for i in range(halfsize,-1,-1):
        for j in range(halfsize-i, halfsize+i+1):
            get +=origin_harvest[size-1-i][j]
    
    print('#',end='')
    print(k, end=' ')
    print(get)
    k = k + 1
    



    
