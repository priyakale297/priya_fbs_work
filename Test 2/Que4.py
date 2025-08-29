# Program to calculate total cost of painting 4 walls

length = float(input("Enter length of the room (m): "))
breadth = float(input("Enter breadth of the room (m): "))
height = float(input("Enter height of the room (m): "))
cost_per_sqm = float(input("Enter cost of painting per sq. meter (Rs): "))

# Calculate area of 4 walls
area_walls = 2 * height * (length + breadth)

#Calculate total cost
total_cost = area_walls * cost_per_sqm

print("Total area of 4 walls =", area_walls, "sq.m")
print("Total cost of painting = Rs", round(total_cost, 2))