x=int(input('input:'))
def sum_of_naturnalnumbers(n):
    if n==1:
        return 1
    else:
        return n+sum_of_naturnalnumbers(n-1)
print(sum_of_naturnalnumbers(x))  # sum of first n natural numbers 
def sum_of_naturnalnumbers2(n):
    if n==0:
        return 0
    return n*(n+1)//2
print(sum_of_naturnalnumbers2(x))  # sum of first n natural numbers using formula 
def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)
print(fibonacci_series(x))  # fibonacci series 
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(x))  # factorial of a number 
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(x,x))  # gcd of two numbers 


