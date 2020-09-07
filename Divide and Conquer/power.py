# Python3 code for extended version 
# of power function that can work 
# for float x and negative y 
  
def power(x, y): 
  
    if(y == 0): return 1
    temp = power(x, int(y / 2))  
      
    if (y % 2 == 0): 
        return temp * temp 
    else: 
        if(y > 0): return x * temp * temp 
        else: return (temp * temp) / x 
      
# Driver Code 
x, y = 2, 3
print('%.6f' %(power(x, y))) 