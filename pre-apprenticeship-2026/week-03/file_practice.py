def read_sales_file(filename):
    with open (filename, "r") as file:
        contents = file.read()
    return contents
try:
    sales_data = read_sales_file("sample.txt")
except FileNotFoundError:
    print ("This file was not found")
else:
    print(sales_data)

def read_sales_lines(filename):
    with open (filename, "r") as file:
        for line in file:
            print(line, end="")
read_sales_lines("sample.txt")