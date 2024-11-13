





def binarySearch(arr,low_bound,upp_bound,search_elem):
    print(arr)
    mid = low_bound+upp_bound/2
    if(arr[int(mid)] == search_elem):
        pos=mid
        return int(pos)
    elif(arr[int(mid)] > search_elem):
        return binarySearch(arr,low_bound,mid-1,search_elem)
    else:
        return binarySearch(arr,mid+1,upp_bound,search_elem)















lengthArr = int(input("Enter the lendth of the array"))
arr=[]
for i in range(lengthArr):
    r=int(input())
    arr.append(r)
    
    
print(arr)



search_elem=int(input("enter a element to search"))
arr = sorted(arr)  # we sorting because binary search only deals with sorted array
print(arr)

pos=binarySearch(arr,0,len(arr),search_elem)
print(pos)




