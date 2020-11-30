def fibonacci(n):
    if type(n)!= int:
        return 'Invalid Input'
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)    
   

def lucas(n) : 
    if type(n)!= int:
        return 'Invalid Input'
    a = 2
    b = 1
      
    if (n == 0) : 
        return a 
   
    # generating number 
    for i in range(2, n + 1) : 
        c = a + b 
        a = b 
        b = c 
      
    return b 

def sum_series(n,value1=0,value2=1):
    if type(n)!= int:
        return 'Invalid Input'
    if type(value1)!= int:
        return 'Invalid Input' 
    if type(value2)!= int:
        return 'Invalid Input'        
    if n==0:
        return value1   
    if n==1:
        return value2     
    return  sum_series(n-1,value1,value2)+sum_series(n-2,value1,value2)
 
  