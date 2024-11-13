
import numpy as np


#creating single dimentional array in array implementation

single_arr = np.array([1, 4, 5, 6])
print("A Single Dimentional Array",single_arr) # it just print that array 

print("Array Shape",single_arr.shape)  # it indicate how many elemens available in the array 

print("Accesing the array 2nd element",single_arr[1])





#creating two dimentional array in array implementation

two_arr = np.array([[1, 4, 5, 6], [3, 4, 6, 7]])
print("A Single Dimentional Array",single_arr) # it just print that array 

print("Array Shape",two_arr.shape)  # it indicate how many elemens available in the array 

print("Accesing the  2nd element in 2nd array",two_arr[1,1])


#create three dimentional array in array implementation 

three_arr = np.array([[[1, 4, 5, 6], [3, 4, 6, 7]], [[10, 40, 50, 60], [30, 40, 60, 70]]])
print("A Three Dimentional Array",three_arr) # it just print that array 

print("Array Shape",three_arr.shape)  # it indicate how many elemens available in the array 

print("Accesing the  2nd element in three_arr in 2nd set in 2nd list ",three_arr[1,1,3])
