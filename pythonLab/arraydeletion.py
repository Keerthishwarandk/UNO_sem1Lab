print("ARRAY INSERTION")

n = int(input("enter the array length"))
 
myarr = []
 
for i in range(n):
    a=int(input())
    myarr.append(a)
    
print(myarr)

print("now you have to delete the array")

delelem = int(input("enter value want to delete"))


#array deletion code
print(f"the number {delelem} from the array {myarr} is deleteted" )

myarr.remove(delelem)
print(f"Array {myarr} After Deletion" )