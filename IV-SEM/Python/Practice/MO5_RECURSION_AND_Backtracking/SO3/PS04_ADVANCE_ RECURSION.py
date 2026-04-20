# digital root 
def digital_root(n):
    if n<10:
        return n  # o(n) is the complexity 
    return digital_root(sum(int(digit) for digit in str(n)))
print(digital_root(10000000000))    
# recurive checking array is sorted or not 
def array_is_sorted(nums):
    return True if nums==nums.sort() else False
print(array_is_sorted([1,4,5,6,2,3,4]))     # o(n) is the time complexity 
