# Validate sales data
def validate_sales(sales):
    if not isinstance(sales, list):
        print("sales must be a list")
        return False
    if not sales:
        print("sales must not be empty")
        return False
    for sale in sales:
        if not isinstance(sale, dict):
            print("sale must be a dictionary")
            return False
        if "product" not in sale:
            print("Product must be in sale")
            return False
        if "quantity" not in sale:
            print("Quantity must be in sale")
            return False
        if "price" not in sale:
            print("Price must be in sale")
            return False
        if type(sale["product"]) != str:
            print("Product must be a string")
            return False
        if not sale["product"]:
            print("product must not be empty")
            return False
        if type(sale["quantity"]) != int:
            print("Quantity must be an integer")
            return False
        if sale["quantity"] <= 0:
            print("quantity must be positive")
            return False
        if type(sale["price"]) != int and type(sale["price"]) != float:
            print("Price must be an integer or a float")
            return False
        if sale["price"] <= 0:
            print("price must be positive")
            return False
    return True

if __name__ == "__main__":
    test_sales = [{"product": "Laptop", "quantity": 3, "price": 1200}]
    result = validate_sales(test_sales)
    print(result)