global get
T = int(input())
k = 1        


         


def dfs(x, y):
    global get
    board[x] = y
    x +=1
       
    
  
    
    if x == num:
        print(board)
        get +=1
        return 0;
    
    
    for i in range(num):
        check = True
        
        for j in range(x):
                  
            if board[j]== i or abs(x-j)== abs(i -board[j]):
                
                check = False
                break;
                        
        

       
            
        
            
                
            
        if check == True:
            
            dfs(x,i)
            
            
        

        


        
   

   

    

for i in range(T):
    global get
    get = 0 
    num = int(input())
    board = [0 for j in range(num)]
    for i in range(num):
        dfs(0,i)

        
        
    print('#',end='')
    print(k, end=' ')
    print(get)
    k +=1
