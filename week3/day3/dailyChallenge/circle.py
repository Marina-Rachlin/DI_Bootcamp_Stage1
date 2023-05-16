import math
from pprint import pprint
import turtle

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them


class Circle:
    def __init__(self, radius = None, diameter = None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either the radius or the diameter.")  

    # Compute the circle’s area
    def area(self):
        return round((math.pi * self.radius ** 2), 2) # round the number to two decimal digits
    
    
    # Print the circle and get something nice

    # option 1
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
     # option 2
    def print_circle(self):
        return pprint(vars(self))
    
     # option 3
    def draw_circle(self):
        my_turtle = turtle.Turtle()
        my_turtle.color("blue")
        my_turtle.pensize(6)
        turtle.speed(0)  
        my_turtle.circle(self.radius * 37.8) # the documentation for turtle.setup indicates that size parameters, if expressed as integers, are pixels and 1 cm = 37.8px
        turtle.done()

    # Method adds two circles together
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type for +: 'Circle' and " + str(type(other)))
        
    # Method compares two circles to see which is bigger
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Unsupported operand type for <: 'Circle' and " + str(type(other)))
        
    # Method compares two circles and see if there are equal
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Unsupported operand type for ==: 'Circle' and " + str(type(other)))
        
    # Method puts the circles in a list and sort them    
    @staticmethod
    def sort_circles(circles):
        sorted_circles = sorted(circles, key=lambda circle: circle.radius)
        sorted_circles_strings = [str(circle) for circle in sorted_circles]
        return print('; '.join(sorted_circles_strings))


circle1 = Circle(radius=5)
circle2 = Circle(radius=3)
circle3 = Circle (radius = 10)

print(circle1.radius)       
print(circle1.area())     
print(circle2)  
circle2.print_circle() 
circle2.draw_circle()
circle3 = circle1 + circle2
print(circle3)
print(circle1 < circle2)    
print(circle1 == circle3)  
circles = [circle1, circle2, circle3] 
sorted_circles = Circle.sort_circles(circles)
