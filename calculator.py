def add(number_viens, number_divi):
    """Add function."""
    return number_viens + number_divi

def multiplnumber_divi(number_viens, number_divi):
    return number_viens * number_divi

print("Select operation.")
print("1.Add")
print("2.Multiply")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplnumber_divi(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        nenumber_vienst_calculation = input("Let's do nenumber_vienst calculation? (number_divies/no): ")
        if nenumber_vienst_calculation == "no":
          break
    
    else:
        print("Invalid Input")