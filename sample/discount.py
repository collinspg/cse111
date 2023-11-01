from datetime import datetime

#core_requirement
# discount_rate = 0.10
# sales_tax_rate = 0.06

# subtotal = float(input("Please enter the subtotal: "))

# current_date_and_time = datetime.now()
# weekday = current_date_and_time.weekday()

# if subtotal >= 50 and (weekday == 1 or weekday == 2):
#     discount = round(subtotal * discount_rate, 2)
#     print(f"Discount amount: {discount:.2f}")
#     subtotal -= discount

# sales_tax = round(subtotal * sales_tax_rate, 2)
# print(f"Sales tax amount: {sales_tax:.2f}")

# total = subtotal + sales_tax

# print(f"Total: {total:.2f}")

#Stretch Challenge
discount_rate = 0.10
sales_tax_rate = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    price = float(input("Please enter the price: "))
    if price != 0:
        quantity = int(input("Please enter the quantity: "))

        subtotal += price * quantity

        print()

subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

current_date_and_time = datetime.now()


weekday = current_date_and_time.weekday()

if weekday == 1 or weekday == 2:
    if subtotal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount


sales_tax = round(subtotal * sales_tax_rate, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax


print(f"Total: {total:.2f}")


