

print("ARRAY Merge Or Array Sort")

a = int(input("enter 1 for array merge or enter 2 for array sort"))

if a == 1:
    print("array merge")
    arr1=[] # array 1 declaration
    arr2=[] # array 2 declaration
    arr1n = int(input("enter the array 1 length"))
    
    for i in range(arr1n):
        a=int(input())
        arr1.append(a)
        
    arr2n = int(input("enter the array 2 length"))
    
    for i in range(arr2n):
        a=int(input())
        arr2.append(a)
        
    arr1.extend(arr2)   
    print(arr1)


if a == 2:
    print("array merge")
    arr=[] # array 1 declaration
    arrn = int(input("enter the array length"))
    
    for i in range(arrn):
        a=int(input())
        arr.append(a)
        
        
    sorted_arr= sorted(arr)   
    print(sorted_arr)    
        
        
        
 