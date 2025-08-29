# Program to calculate total bill with 18% GST

S = int(input("Enter number of products: "))

total_price = 0
for i in range(1, S+1):
    price = float(input(f"Enter price of product {i}: "))
    total_price += price

gst = total_price * 0.18

final_bill = total_price + gst

print("Total price before GST = Rs", round(total_price, 2))
print("GST @18% = Rs", round(gst, 2))
print("Final Bill Amount = Rs", round(final_bill, 2))