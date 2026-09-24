from sales.validator import validate_sales
import json
with open ("sample.json", "r") as file:
    sales_data = json.load(file)
    print(sales_data)
    print(type(sales_data))
   

product = {"product": "Keyboard", "quantity": 5, "price": 75}
with open("output.json", "w") as file:
    json.dump(product, file, indent=1)

with open ("sales.json", "r") as file:
    try:
        sales_data = json.load(file)
    except json.JSONDecodeError:
        print("Please fix error in Json file")
    else:
        print(sales_data)
        print(type(sales_data))
        valid_sales = validate_sales(sales_data)
        print(valid_sales)
