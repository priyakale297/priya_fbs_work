# Function to calculate area of a circle
import math
def calculate_circle_area(radius):
    area =  math.pi * radius ** 2
    return area


radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)

print(f"The area of the circle is: {area:.2f}")