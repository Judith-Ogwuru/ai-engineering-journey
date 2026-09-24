# Calculate total revenue
def calculate_total_revenue(sales_data):
    total_revenue = 0
    for sale in sales_data:
        total_revenue += sale["quantity"] * sale["price"]
    return total_revenue

# Find highest-value sale
def find_highest_value_sale(sales_data):
    if not sales_data:
        return None
    highest_value = sales_data[0]["quantity"] * sales_data[0]["price"]
    highest_sale = sales_data[0]
    for sale in sales_data:
        if sale["quantity"] * sale["price"] > highest_value:
            highest_value = sale["quantity"] * sale["price"]
            highest_sale = sale
    return highest_sale

# Find lowest-value sale
def find_lowest_value_sale(sales_data):
    if not sales_data:
        return None
    lowest_value = sales_data[0]["quantity"] * sales_data[0]["price"]
    lowest_sale = sales_data[0]
    for sale in sales_data:
        if sale["quantity"] * sale["price"] < lowest_value:
            lowest_value = sale["quantity"] * sale["price"]
            lowest_sale = sale
    return lowest_sale

# Getting products above a certain price
def get_products_above_price(sales_data, minimum_price):
    matching_sales = []
    for sale in sales_data:
        if sale["price"] > minimum_price:
            matching_sales.append(sale)
    return matching_sales

# Getting sales statistics
def get_sales_statistics(sales_data):
    statistics_summary = {}
    statistics_summary["total"] = calculate_total_revenue(sales_data)
    statistics_summary["count"] = len(sales_data)
    if not sales_data:
        statistics_summary["average"] = None
        statistics_summary["maximum"] = None
        statistics_summary["minimum"] = None
        return statistics_summary
    statistics_summary["average"] = statistics_summary["total"] / statistics_summary["count"]
    highest_sale = find_highest_value_sale(sales_data)
    statistics_summary["maximum"] = highest_sale["quantity"] * highest_sale["price"]
    lowest_sale = find_lowest_value_sale(sales_data)
    statistics_summary["minimum"] = lowest_sale["quantity"] * lowest_sale["price"]
    return statistics_summary



