def  palindrome(n):
    return True if n== ''.join(reversed(n)) else False
n=input('input')
print(palindrome(n))
a=[10,20,30,40,50,60,70,10]
res=list(filter(lambda x: x&1==0,a))
print(res)
print(set(a))
def sum_of_digits(n):
    return sum(int(d) for d in n)
print (sum_of_digits(n))
# alphabet question 
ass=['a','c','d','o','x']
print(sorted(ass))
#coomon elements 
