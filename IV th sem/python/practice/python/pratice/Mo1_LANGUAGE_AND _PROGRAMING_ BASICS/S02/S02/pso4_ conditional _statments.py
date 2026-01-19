# even or odd
def check(n):
    if (1&n)==0:
        return True
n=int(input())
print('even' if check(n) else'odd' )    
# prime number 
import math 
def prime(n):
    if n==2:
      return True
    for i in range (2,int(math.sqrt(n))+1,1):
        # if n==2:
        #     break
        #     return True
        if n%i==0:
          break
          return False
print("prime " if prime(n) else "not prime")       



        
    
    