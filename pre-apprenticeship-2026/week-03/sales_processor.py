from sales.validator import validate_sales
sales = [{"product": "Laptop", "quantity": 3, "price": 1200}]
result = validate_sales(sales)
print(result)
