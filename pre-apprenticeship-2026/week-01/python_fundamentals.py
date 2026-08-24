# ==============================
# Week 1 —— Python Fundamentals
# ==============================

# ==============================
# 1. Variables and Types
# ==============================

name = "Judith"
age = 30
scores = [85, 92, 88]

print(type(name))
print(type(age))
print(type(scores))

# ==============================
# 2. Type Conversion
# ==============================

value = "42"

print(value)
print(type(value))

number = int(value)

print(number)
print(type(number))

# ==============================
# 3. Type Errors
# ==============================

value = "42"
number = 8

# This would cause a TypeError because value is a string and number is an integer

# answer = value + number
# print(answer)

# Convert value fron a string to an integer first
answer = int(value) + number

print(answer)

# ==============================
# 4. Expressions
# ==============================

x = 10
y = 5

sum_result = x + y
difference = x - y
product = x * y
quotient = x / y

print(sum_result)
print(difference)
print(product)
print(quotient)

# ==============================
# 5. Input and Output
# ==============================

name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
age = int(age)

print(age)
print(type(age))

# ==============================
# 5. Conditionals
# ==============================

score = 85
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
else:
    print("Needs improvement")

