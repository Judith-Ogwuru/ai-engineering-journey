try:
    price = float(input("Enter the price (decimals are accepted): "))
    if price <= 0:
        raise ValueError
    print("The price is", price)
except ValueError:
    print("Please enter a valid price.")
