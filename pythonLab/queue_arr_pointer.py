class queue_in_array:
    def __init__(self):
        self.queue = []
        
    def push_op_in_queue(self):
        a = int(input("Enter Queue Length"))  #length of array 
        for i in range(a):
            elem=int(input(f"Enter thr QueElement {i+1}  "))   #getting each element
            self.queue.append(elem)
        print(f"Queue after push {self.queue}")
    def pop_queue(self,flag):
        print(flag)
    
        while(flag and self.queue):
            self.queue.pop(0)
            print(f"Queue after pop {self.queue}")
            print(f"Leangth {len(self.queue)}")
            self.req_pop()
                                                                                                               

            
    def req_pop(self):
        req=input("Are you want to pop Y[yes] N[No]")
        if req.lower() == "y" or req.upper() == "Y":
            flag=bool(1)
            if not self.queue:
                print("Queue is underflow")  
            else:
                self.pop_queue(flag)
           
        elif req.lower() == "n" or req.upper() == "N":
            flag=bool(0)
            self.pop_queue(flag)
           
          
       
               
obj = queue_in_array()
obj.push_op_in_queue()
obj.req_pop()
