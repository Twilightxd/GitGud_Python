# This file is pushed using VSCode
# Practice for Lists and Functions

# Smaple Function syntax
def greet(name):
    return f"Hello, {name}!"
print(greet("GitGud"))

# Find the largest number in list 
num = [5, 10, 15, 8, 21]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("Largest number is: ", largest)

# Find the smallest number in list 
num = [5, 10, 25, 2, 66]
smallest = num[0]
for i in num:
    if i < smallest:
        smallest = i
print("Smallest number is: ", smallest)

# Check prime using function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, " is a prime numebr")
else:
    print(number, " is not a prime number")

# Simple Calculator (add, subtract, multiply, divide)
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def remainder(x, y):
    return x % y

print("Select operation: 1.ADD 2.SUBTRACT 3.MULTIPLY 4.DIVIDE 5.REMAINDER")
choice = input("Enter your choice - 1, 2, 3, 4, 5 >> ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
elif choice == '5':
    print(remainder(num1, num2))
else:
    print("Wrong Input")