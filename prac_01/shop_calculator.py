
TOTAL_PRICE = 0

number_of_items = float(input("Number of items: "))
total_number_of_items = number_of_items
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = float(input("Number of items: "))
    total_number_of_items = number_of_items
while number_of_items > 0:
    price_of_item = float(input("Price of item: "))
    TOTAL_PRICE = TOTAL_PRICE + price_of_item
    number_of_items = number_of_items - 1
if TOTAL_PRICE > 100:
    TOTAL_PRICE = TOTAL_PRICE * 0.9
print(f"Total price for {total_number_of_items:.0f} items is ${TOTAL_PRICE:.2f}")