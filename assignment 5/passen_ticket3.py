# Program to calculate total ticket cost with discounts

n = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range(1, n+1):
    age = int(input(f"Enter age of passenger {i}: "))
    
    if age < 12:  # Children
        cost = ticket_cost * 0.70   # 30% discount
    elif age > 59:  # Senior citizen
        cost = ticket_cost * 0.50   # 50% discount
    else:  # Others
        cost = ticket_cost
    
    print(f"  Ticket cost for passenger {i}: {cost:.2f}")
    total_amount += cost
print(f"\nTotal Ticket Amount for all passengers: {total_amount:.2f}")