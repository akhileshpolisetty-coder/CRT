#LINEAR SEARCHNG 
def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(linear_search([1,2,3,4,5],3), 'yes' if linear_search([1,2,3,4,5],3) != -1 else 'no') # time complexity o(n)
  # second largest element 
def second_largest(nums):
   return sorted(nums)[-2] 
print(second_largest([1,2,3,4,5])) # time complexity o(n log n)
def largest_loop(nums):
    largest=nums[0]
    for i in range (len(nums)):
        if largest< nums[i]:
            largest=nums[i]
    return largest 
print(largest_loop([1,2,3,4,5])) # time complexity o(n)           
# binary search works on sorted array 
def binary_search(nums,target):
    start=0;end=len(nums)-1
    while(start<=end):
        mid = (start+end)//2
        if nums[mid]==target:
            print("found")
            return mid 
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1 
print(binary_search([1,2,3,4,5],3)) # time complexity o(log n)         
def reverse(nums):
    start = 0
    last = len(nums) - 1
    while start < last:
        temp = nums[last]
        nums[last] = nums[start]
        nums[start] = temp
        start += 1
        last -= 15
    return nums

print(reverse([1, 2, 3, 4, 5]))  # time complexity o(n) # space complixity o(1)

 
