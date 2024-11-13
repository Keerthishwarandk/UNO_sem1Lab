class setmanipulation:
    def __init__(self):
        self.theSet=set(())
        self.theSett=set(())

        length_one = int(input("Enter the length of the Set 1 - "))
        length_two = int(input("Enter the length of set 2 - "))

        for i in range(length_one):
            a=int(input(f"Enter the set value {i+1} - "))
            self.theSet.add(a)
            
        for j in range(length_two):
            b=int(input(f"Enter the set value {j+1} - "))
            self.theSett.add(b)
    def showSet(self):
        print("You Set 1"," ",self.theSet)
        print("You Set 2"," ",self.theSett)
        
    def searchElementinSet():
        searchfor=int(input("Enter the Value to Search"))
        if(searchfor in self.theSet):
            print(f"The given element {searchfor} found in Set")                     
        else:
            print(f"the give element {searchfor} not found")           
            
    def setUnion(self):
        union = self.theSet | self.theSett   #union of sets means have to use this | operator 
        print("Union of two set it combines elements from two given sets"," ",union)
        
    def inser_section(self):
        inter_Section=self.theSet & self.theSett  #inster section of two set have to print common element in two sets  use & for that 
        print("The common element in the given both sets"," ",inter_Section)  
        
    def deffrence(self):
        def_ference = self.theSet - self.theSett # dirrece in set A and set B Element in set a not in Set B
        print(f"Element in set a not in Set B",def_ference)
        
    def symentric(self):
        symentric = self.theSet ^ self.theSett# elements either in setA setB  not in both 
        symentric_format = "{:>10}".format(symentric)
        print("Elemnts either in set 1 and set 2  or Elemnts not in Both Set",symentric_format)
obj = setmanipulation()
obj.showSet()




def getflag():
    msg = input("Do You want to perform Action Yes[Y] or No[N]")
    if msg =="Y":
        flag = bool(1)
        return flag
    else:
        flag =bool(0)
        return flag
        
flag = getflag()
while flag:
    action = input("Enter the manipulation perform in the two sets Enter U for union [or] I for insersection [or] D for Diffrence [or] S for Symentric Diffrence")
    match action:
        case "I":
            obj.inser_section()
            flag = getflag()
        case "U":
            obj.setUnion()
            flag = getflag()
        case "D":
            obj.deffrence()
            flag = getflag()
        case "S":
            obj.symentric()
            flag = getflag()

