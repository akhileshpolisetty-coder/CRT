# count number of digits
x=input('input').strip()
print(len(x)) 
#### sum of all digits 
def sum_of_digits(x):
    return sum(int(d) for d in str(x))
print(sum_of_digits(x))
########### nxt question 
def print_even_and_odd(x):
    return sum(int(d)%2==0 for d in str(x)),sum(int(d)%2 !=0 for d in str(x))  #o(n) is better 
print(print_even_and_odd(x))
############ nxt question 
def sum_of_give(x):
    return x if x < 10 else sum_of_give(sum(int(d) for d in str(x)))
print(sum_of_give(int(x)))
####cdigit 
def reverse_of_the_number(x):
    return -1  if int(x)<0 else int(x[::-1])
print(reverse_of_the_number(str(x)))