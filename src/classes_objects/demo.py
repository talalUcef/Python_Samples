'''
Created on 2 août 2015

@author: talalUcef
'''
# create a clas
class Point(object):
    ''' Represent a point in 2D space .'''
        
print(Point)

# crate an instance
blank = Point()
print(blank)

# attributes
blank.x = 3.0
blank.y = 4.0

print("(", blank.x, ",", blank.y, ")")

def print_point(p):
    print("(%g, %g)" % (p.x, p.y))
          
print_point(blank)

class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

center = find_center(box)
print_point(center)

