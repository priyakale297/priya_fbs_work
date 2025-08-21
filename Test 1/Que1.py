#Accept the user

length = int(input("Enter the length:"))
breadth = int(input("Enter the breadth:"))
radius = int(input("Enther the radius:"))

#rect calculation
rect_area = length * breadth
rect_perimeter = 2 * (length + breadth)

#circle calculation
circle_area =  radius**2
circle_circumference = 2 * radius

print(f'Reactangle area:')
print(f'Rectangle perimeter:')
print(f'circle area:')
print(f'circle circumference:')