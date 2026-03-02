li=[1,2,3,4,5]
res=[]
for element in li:
    element*=2
    res.append(element)
print(res) 
print([i for i in li if i%2==0])   
lii=['a','b','c']
print(''.join(lii))
n = 4
# Top half (Pyramid)
for i in range(1, n+1):
    print('-' * (n-i) + '*' * (2*i-1))

# Bottom half (Inverted Pyramid)
for j in range(n-1, 0, -1):
    print('-' * (n-j) + '*' * (2*j-1))

n = 4
for i in range(1, n + 1):
   
    print(" " * (n - i), end="")
    

    for j in range(1, i + 1):
        print(chr(64+i), end=" ")
    
    print() # New line


