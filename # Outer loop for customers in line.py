
while True:
    total = 0

    customer_name = input("Enter customer name: ")

    while True:
        quantity = int(input("Enter the quantity of the item: "))
        items = float(input("Enter the price of the item: "))
        item_total = quantity * items
        total += item_total
        repeat = input("Do you want to add more items to the cart (Y/y for Yes, N/n for No): ")

        if repeat.lower() == 'n':
            break

    print("Customer: ", customer_name)
    print("Total Amount: $", total)

    new_customer = input("Go to the next person (Y/y for Yes, N/n for No): ")

    if new_customer.lower() == 'n':
        break
