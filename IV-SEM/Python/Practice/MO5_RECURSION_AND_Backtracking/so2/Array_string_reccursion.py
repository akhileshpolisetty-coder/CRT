def sum_of_array(arr,n):
    if n==0:
        return 0
    return arr[n-1]+sum_of_array(arr,n-1)
print(sum_of_array([1,2,3,4,5],5))  # sum of array 


def sum_of_array(arr):
    return sum(arr)
print(sum_of_array([1,2,3,4,5]))  # sum of array 
def reverse_array(arr):
    return arr[::-1]
print(reverse_array([1,2,3,4,5]))  # reverse array 

def reverse_a_string(s):
    if len(s)==0:
        return s
    return reverse_a_string(s[1:])+s[0]    
print(reverse_a_string("hello"))  # reverse a string 


