name = input("Enter Customer Name: ")
units = float(input("Enter Electricity Units: "))

if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = (100 * 3) + (units - 100) * 5
elif units <= 300:
    bill = (100 * 3) + (100 * 5) + (units - 200) * 7
else:
    bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

print("\n----- Electricity Bill -----")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Total Bill: Rs.", bill)
