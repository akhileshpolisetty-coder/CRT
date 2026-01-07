# bitwise operators 
x=int(input())
print(x<<2)# left shift
print(x>>2) # right shift
print(~x) # onse complement
# member ship operator in and not in
li=[10,20,30,40,100]
if 100 in li:   # membership opeartor to check iterable objects 
    print("good morning ")
x= "hello"
if any(vowel in x for vowel in ['a','e','i']):
              print ("good morning")                    
''' reference countinting if any object-> reference count>0 then the object is there  '''              