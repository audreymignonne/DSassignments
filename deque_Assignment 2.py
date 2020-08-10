import numpy

class deque:

    def __init__(self):
        self.args = []
        self.max = 20

    def add_to_front(self, x):
        if len(self.args) == self.max:
            return "Deque is full!"
        else:
            self.args.insert(0,x)
        
    def add_to_back(self, x):
        if len(self.args) == self.max:
            return "Deque is full!"
        else:
            self.args.append(x)

    def remove_front(self):
        if self.args != []:
            self.args.pop()
        else:
            return "Deque is empty!"
        
    def remove_back(self):
        if self.args != []:
            self.args.pop(0)
        else:
            return "Deque is empty!"
        
    def num_elements(self):
        if self.args == []:
            return None
        elif len(self.args) == self.max:
            return "deque is full!"
        else:
            return len(self.args)
    
    def last(self):
        return self.args[-1]
    
    def first(self):
        return self.args[0]
    def isEmpty(self):
        
        if(self.values) == []:
            return True
        else:
            return False
    
   
    
 
 #assuming sequence of deque are random integer numbers between 1, 100       
if __name__ == "__main__":
    a = deque()
    new = numpy.random.randint(1,100, 1)
    a.add_to_front(new)

    print("The number of elements in the deque is", a.num_elements())
    
    b = a.remove_front()
    print(b)
    
    deque2 = deque()
    elem = numpy.random.randint(1,100)
    print(deque2.num_elements())