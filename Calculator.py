# This function adds two numbers
def add(x, num_2):
    return num_1+ num_2

# This function subtracts two numbers
def subtract(x, num_2):
    return num_1- num_2

# This function multiplies two numbers
def multiplnum_2(x, num_2):s
    return num_1* num_2

# This function divides two numbers
def divide(x, num_2):
    return num_1/ num_2



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplnum_2")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        trnum_2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplnum_2(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (num_2es/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")