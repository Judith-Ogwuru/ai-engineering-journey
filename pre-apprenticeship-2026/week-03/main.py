from sales.reader import read_sales_csv, read_sales_json
from sales.validator import validate_sales
from sales.processor import get_sales_statistics, find_highest_value_sale, find_lowest_value_sale
from sales.reporter import create_report, display_report, save_report
import json

while True:
    print("Sales Processor")
    print()
    menu_display = ["1. Load CSV sales data", "2. Load JSON sales data", "3. Exit"]
    for menu in menu_display:
        print(menu)
    try:   
        menu_choice = int(input("Select a menu: "))
    except ValueError:
            print("Please enter a valid number")
    else:
        try:
            if menu_choice == 1:
                sales_data = read_sales_csv("data/sales.csv")
                break
            elif menu_choice == 2:
                sales_data = read_sales_json("data/sales.json")
                break
            elif menu_choice == 3:
                break
            else:
                print("Please select 1, 2 or 3")
        except json.JSONDecodeError:
            print("Please review your json file for error")
        except ValueError:
            print("The sales file contains invalid numeric data")
        except FileNotFoundError:
            print("The sales file was not found")
            
if menu_choice == 1 or menu_choice == 2:
    valid_sales_data = validate_sales(sales_data)
    if valid_sales_data:
        print("The sales data is valid")
        sales_statistics = get_sales_statistics(sales_data)
        highest_value_sale = find_highest_value_sale(sales_data)
        lowest_value_sale = find_lowest_value_sale(sales_data)
        sales_report = create_report(sales_statistics, highest_value_sale, lowest_value_sale)
        display_report(sales_report)
        save_report(sales_report, "output/sales_report.json")
    else:
        print("The sales data is invalid")

