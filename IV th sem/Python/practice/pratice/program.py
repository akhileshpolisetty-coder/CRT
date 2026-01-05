def  iseven(n):
    if (1 & n)==0:   # bit wise operation to find even and odd 
        print("even")
    else:
        print("odd")
n=int(input())
iseven(n)            

# (1 & n)==0 then its even or its odd its the optimal solution 
# import math
# def isprime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2,int((math.sqrt(n)+1)):
#             if (n%i)==0:
#                 return True
# print("prime " if isprime(11) else "not prime")            
            