from sales.validator import validate_sales
import csv

def read_sales_csv(filename):
    sales_data = []
    with open (filename, "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            quantity = int(row["quantity"])
            price = float(row["price"])
            sale = {"product": row["product"], "quantity": quantity, "price": price}
            sales_data.append(sale)
    return sales_data

try:
    sales = read_sales_csv("sales.csv")
except FileNotFoundError:
    print("The file was not found")
except ValueError:
    print("The sales file contains invalid numeric data")
else:
    print(sales)
    updated_sales = validate_sales(sales)
    print(updated_sales)