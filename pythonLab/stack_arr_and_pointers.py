print("Stack operation using stackay ")
print("Stack push operation")
length =  int(input("Enter stackay Length"))
stack=[]
for i in range(length):
    a=int(input(f"Enter element {i+1} "))
    stack.append(a)
 
print("stackay After push",stack) 


print("Stack pop operation")
flag = bool(1)
while flag:
    stack.pop()
    print("stackay After pop",stack) 
    a = input("Do you want pop Yes Y or No N")
    if a.upper() == "N":
        flag=bool(0)
    else:
        flag=bool(1)
        
        
        
