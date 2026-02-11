import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10);arr.append(20)
print(arr)
s=input()
print(sum(int(d) for d in s))