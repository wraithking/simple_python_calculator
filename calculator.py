def add(number1, number2):
    """Add function."""
    return number1 + number2

def multiplication(number1, number2):
    """Multiplication function."""
    return number1 * number2

print("Select operation.")
print("1. Add")
print("2. Multiply")
print("3. Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")

    if choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    
    else:
        print("Invalid Input")
