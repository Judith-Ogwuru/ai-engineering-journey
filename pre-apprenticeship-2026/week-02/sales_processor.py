# Sales data
sales = [{"product": "Laptop", "quantity": 3, "price": 1200},
         {"product": "Mouse", "quantity": 10, "price": 25},
         {"product": "Keyboard", "quantity": 5, "price": 75},
         {"product": "Monitor", "quantity": 2, "price": 300}]

# View sales
def view_sales(sales):
    return sales

# Calculate total revenue
def calculate_total_revenue(sales):
    total_revenue = 0
    for sale in sales:
        total_revenue += sale["quantity"] * sale["price"]
    return total_revenue

# Find highest-value sale
def find_highest_value_sale(sales):
    if not sales:
        return None
    highest_value = sales[0]["quantity"] * sales[0]["price"]
    highest_sale = sales[0]
    for sale in sales:  
        if sale["quantity"] * sale["price"] > highest_value:
            highest_value = sale["quantity"] * sale["price"]
            highest_sale = sale
    return highest_sale

# Get products above price
def get_products_above_price(sales, minimum_price):
    above_price = []
    for sale in sales:
        if sale["price"] > minimum_price:
            above_price.append(sale)
    return above_price

# Get sales statistics
def get_sales_statistics(sales):
    summary = {}
    summary["total"] = calculate_total_revenue(sales)
    summary["count"] = len(sales)
    if not sales:
        summary["average"] = None
        summary["maximum"] = None
        summary["minimum"] = None
        return summary
    summary["average"] = summary["total"] / summary["count"]
    maximum = sales[0]["quantity"] * sales[0]["price"]
    minimum = sales[0]["quantity"] * sales[0]["price"]
    for sale in sales:
        if sale["quantity"] * sale["price"] > maximum:
            maximum = sale["quantity"] * sale["price"]
        if sale["quantity"] * sale["price"] < minimum:
            minimum = sale["quantity"] * sale["price"]
    summary["maximum"] = maximum
    summary["minimum"] = minimum
    return summary

# Helper function
def display_sale(sale):
    print(sale["product"], "-", "Quantity:", sale["quantity"], "-", "Price:", f"${sale["price"]:,.2f}")

# Main program
menu_display = ["1. View sales", "2. Calculate total revenue", "3. Find highest-value sale", "4. Find products above price", "5. View sales statistics", "6. Exit"]
while True:
    print("Sales Processor")
    print()
    for menu in menu_display:
        print(menu)
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            all_sales = view_sales(sales)
            for sale in all_sales:
                display_sale(sale)
        elif choice == 2:
            total_revenue = calculate_total_revenue(sales)
            print("Total revenue:", f"${total_revenue:,.2f}")
        elif choice == 3:
            highest_sale = find_highest_value_sale(sales)
            if highest_sale is None:
                print("No highest-value sale")
            else:
                print("Highest-value sale:", highest_sale["product"], "-", "Quantity:", highest_sale["quantity"], "-", "Price:", f"${highest_sale["price"]:,.2f}", "-", "Sale_value:", f"${highest_sale["quantity"] * highest_sale["price"]:,.2f}")
        elif choice == 4:
            while True:
                try:
                    minimum_price_choice = int(input("Enter minimum price: "))
                    if minimum_price_choice <= 0:
                        print("Price must be positive")
                    else:
                        break
                except ValueError:
                    print("Invalid input")
            filtered_sales = get_products_above_price(sales, minimum_price_choice)
            if not filtered_sales:
                print("No products found above that price")
            for item in filtered_sales:
                display_sale(item)
        elif choice == 5:
            sales_summary = get_sales_statistics(sales)
            print("Sales statistics")
            print()
            if sales_summary["count"] == 0:
                print("No sales available")
            else:
                print("Total:", f"${sales_summary["total"]:,.2f}")
                print("Count:", sales_summary["count"])
                print("Average:", f"${sales_summary["average"]:,.2f}")
                print("Maximum:", f"${sales_summary["maximum"]:,.2f}")
                print("Minimum:", f"${sales_summary["minimum"]:,.2f}")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again")
    except ValueError:
        print("Invalid input")



