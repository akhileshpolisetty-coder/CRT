
# read number palindrome, armstrong number, perfect number
def armstrongnumber(n):
    return sum(int(d)**len(n) for d in n) == int(n)
n=input().strip()
print(armstrongnumber(n))
# 2) perect number 
def perfect_number(num):
    if num < 2:
        return False
    return sum(i for i in range(1,num) if num%i==0)==num
num=int(n)
print(perfect_number(num))
# 3) strong number 
import math
def strong_number(num):
    return sum(math.factorial(int(j)) for j in n)==num
print(strong_number(num)) 
# palindrone number 
def palindrome_number(num):
    return int(n[::-1])==num
print(palindrome_number(num))