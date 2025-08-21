l1 = float(input("Enter length of room 1 (m):"))
b1 = float(input("Enter breadth of room 1 (m):"))
l2 = float(input("Enter length of room 2 (m):"))
b2 = float(input("Enter breadth of room 2 (m):"))
h  = float(input("Enter height of walls (m):"))

interior_area = (2* (l1 + b1) + 2 * (l2 + b2)) * h

outer_parameter = (l1 + l2 + 2 * b1) * 2

print(f" interior wall area: sq.m")
print(f"exterior wall area: sq. m")
