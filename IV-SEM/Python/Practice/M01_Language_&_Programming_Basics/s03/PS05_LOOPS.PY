# loops in python
counter=0
while counter <5:
    print("hello world","*")
    counter+=1
counter=1    
n=int(input())
while counter<=n:
    print(counter,end="*")
    counter+=1
print()    
while n>0:
    print(n,end="*")
    n-=1 
k=int(input())
while n<=k:
    if(n & 1)==0:
        print(n)
    n+=1        