class callby_value_refrence:
    def __init__(self):
        self.variable_one = int(input("Enter the actual Value"))
    def call_by_value(self,val):
        self.variable_one=val+1
        print("only Function parameter get updated",self.variable_one)
     
        
    def showvalue(self):
        print(self.variable_one)
        
    def get_variable(self):
        print("original data before modification",self.variable_one)
        return self.variable_one
        
    def getValue(self):
        lis = []
        length = int(input("Call by Refrence can perform in mutable data enter the length "))
        for i in range(length):
            a=input(f"Enter Value {i+1}")
            lis.append(a)
        print("Your immutable Data before modification",lis)
        
        return lis
        
    def call_by_refrence(self,lis):
        a= int(input("enter value to modify"))
        lis.append(a)
       
obj=callby_value_refrence()
value = obj.get_variable()
obj.call_by_value(value)
obj.showvalue()
#print("original data after modification",value)
val2=obj.getValue()
obj.call_by_refrence(val2)
print("original data after modification",val2)