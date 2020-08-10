class Point: #point class to manipulate x,y coordinates
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    
class Rectangle:
    def __init__(self, bottomLeftCorner, topRightCorner): #bottomLeftCorner and topRightCorner as instances of Point class defined above
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightCorner = topRightCorner
        
        self.length = topRightCorner.x - bottomLeftCorner.x
        self.breadth = topRightCorner.y - bottomLeftCorner.y
        
        self.area = self.length*self.breadth
        
        self.perim = (self.length + self.breadth)*2
        
    def intersection(blA, trA, blB, trB):  
        if (blA.x < trB.x or blB.x < brA.x):
            return False

        else:
            return True
        
#testing all cases
a = Rectangle(Point(1,2), Point(5,6))
print("Area", a.area)
print("Perimeter:", a.perim)

#intersection
rectA = Rectangle(Point(8,3), Point(10,5))
rectB = Rectangle (Point(11,2), Point(14,3))
x= Rectangle.intersection(rectA.bottomLeftCorner, rectA.topRightCorner, rectB.bottomLeftCorner, rectB.topRightCorner)
print (x)
