import math
n=int(input('g'))
print(*[i for i in range(1,n+1)if n%i==0])
print(len([j for j in range(1,n+1)if n%j==0]))
# prime number 
print(n>1 and all(n%i==0 for i in range(2,int(n**0.5) +1 )))
def f(n): return 1 if n<2 else  n*f(n-1)
print('not'if n<0 else f(n))


