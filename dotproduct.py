import numpy  
import random  

tenList = [] 
hunList = [] 

def DotProduct(N, ListA, ListB):
   #generate N number of random numbers b/n 1 and 1000 
    for i in range(N):  
        a = random.randint(1, 1000)  
        ListA.append(a)
        
    for j in range(N):  
        b = random.randint(1, 1000)  
        ListB.append(b)  

    product = numpy.dot(ListA, ListB)  

    print("ListA: ", ListA)
    print("ListB: " , ListB)
    print("The Dot Product of both lists each of size", N, "is", product)  

#testing for N=10, 100
DotProduct(10, tenList, hunList)  
DotProduct(100, tenList, hunList)