passoword="admin1234"
attempt=0
max_attemps=3
while attempt<= max_attemps:
    s=input("enter password").strip()
    if passoword==s:
        print("welocome ")
        break
    else:
        attempt+=1
        print("wrong password")    
    if attempt==max_attemps:
        print("get lost")    
