import math 

radius = 20
length = 50
breadth = 40
times = 5
cost_per_meter = 35

print("Length of rectangle =", length)
print("Breadth of radius =", breadth)
print("Radius of half circle =", radius)

#perimeter of rectangle excluding one breadth
rect_perimeter = length + 2 * breadth
print("Rectangle part  of perimeter =", rect_perimeter)

# arc length of half circle
arc_length = math.pi * radius
print("Arc length of half circle =", round(arc_length,3))

#total fencing length
total_length = rect_perimeter + arc_length
print("Total fencing length = ", round(total_length,3))

#facing is done 5 times
total_wire_length = total_length * times
print("Total wire length(5 times) =", round(total_wire_length, 3))

#total cost
total_cost = total_wire_length * cost_per_meter
print("total cost of fencing the field = Rs", round(total_cost,2))