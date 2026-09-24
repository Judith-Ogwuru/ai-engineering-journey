import csv 
import json

# Read sales data from csv
def read_sales_csv(filename):
    sales_data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            quantity = int(row["quantity"])
            price = float(row["price"])
            sale = {"product": row["product"], "quantity": quantity, "price": price}
            sales_data.append(sale)
    return sales_data

# Read sales data from json
def read_sales_json(filename):
    with open(filename, "r") as file:
        sales_data = json.load(file)
    return sales_data













