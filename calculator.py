# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


# Example usage of the calculator functions without user input
num1 = 10
num2 = 5

print(num1, "+", num2, "=", add(num1, num2))
print(num1, "-", num2, "=", subtract(num1, num2))
print(num1, "*", num2, "=", multiply(num1, num2))
print(num1, "/", num2, "=", divide(num1, num2))
