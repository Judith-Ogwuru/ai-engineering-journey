import json

# Create sales report
def create_report(summary, highest_sale, lowest_sale):
    report = {}
    report["total_revenue"] = summary["total"]
    report["number_of_sales"] = summary["count"]
    report["average_revenue"] = summary["average"]
    report["maximum_sale_revenue"] = summary["maximum"]
    report["minimum_sale_revenue"] = summary["minimum"]
    report["highest_value_sale"] = highest_sale
    report["lowest_value_sale"] = lowest_sale
    return report

# Display sales statistics
def display_report(report):
    print("Total revenue:", f"${report["total_revenue"]:,.2f}")
    print("Number of sales:", report["number_of_sales"])
    print("Average revenue:", f"${report["average_revenue"]:,.2f}")
    print("Maximum sale revenue:", f"${report["maximum_sale_revenue"]:,.2f}")
    print("Minimum sale revenue:", f"${report["minimum_sale_revenue"]:,.2f}")
    print()
    print("Highest-value sale:")
    print("Product:", report["highest_value_sale"]["product"])
    print("Quantity:", report["highest_value_sale"]["quantity"])
    print("Price:", f"${report["highest_value_sale"]["price"]:,.2f}")
    print()
    print("Lowest-value sale:")
    print("Product:", report["lowest_value_sale"]["product"])
    print("Quantity:", report["lowest_value_sale"]["quantity"])
    print("Price:", f"${report["lowest_value_sale"]["price"]:,.2f}")    
            
# Save sales report
def save_report(report, filename):
    with open(filename, "w") as file:
        json.dump(report, file, indent=1)
    return True

if __name__ == "__main__":
    with open("output/sales_report.json", "r") as file:
        test = json.load(file)
    display_report(test)




