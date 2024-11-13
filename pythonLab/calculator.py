print("Python Calculatort")

def getoptions():
    print("a for Add : s for Subtraction : m for multiplication : d for Division")
    ops = str(input("Enter the  Action"))
    return ops
    
    
def calculator(ops):
    match ops:
        case "a": 
            a=int(input())
            b=int(input())
            c=a+b
            print(f"Result of {a} + {b} is {c}")
        case "s": 
            a=int(input())
            b=int(input())
            c=a-b 
            print(f"Result of {a} - {b} is {c}")        
        case "m": 
            a=int(input())
            b=int(input())
            c=a*b
            print(f"Result of {a} * {b} is {c}")
        
        case "d": 
            a=int(input())
            b=int(input())
            c=a/b
            print(f"Result of {a} / {b} is {c}")
        case _:
            print("you entered invalid option")
            getoptions()    
flag = bool(1)
while flag:
    ops = getoptions()
    calculator(ops)
    f1=input("Do you  continue yes or no")
    if f1 == "yes":  
        flag = bool(1)
    else:
        flag = bool(0)
        

    
    
    
    


    
