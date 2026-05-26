import math

def circle(radius):
    area = (math.pi)*radius*radius
    circumference = 2*(math.pi)*radius
    return area, circumference
    
r = int(input("enter the Radius: "))
a,c = circle(r)

print(f"\nArea: {round(a, 2)} \nCircumference: {round(c, 2)}")