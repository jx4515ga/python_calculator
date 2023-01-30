#This is a simple calculator,
#able to solve simple math oprations.

# This function is used for adding two numbers
def addition(x, y):

    return x + y

# This function is used for subtracting two numbers
def subtraction(x, y):

    return x - y

# This function is used for multiplying two numbers
def multiplication(x, y):

    return x * y

# This function is used for dividing two numbers
def division(x, y):

    return x / y


# Now we will take inputs from the user
print("Please select the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    user_choice = input("Please enter choice (1, 2, 3, 4): ")
    # User make a select math operation
    if user_choice in ("1", "2", "3", "4"):
        try:

            # User enter number 1 and 3 to complete math operation
            num_1 = int(input("Please enter the first number: "))
            num_2 = int(input("Please enter the second number: "))
        except ValueError:
            print("Invalid input. Please Try Again!")

        if user_choice == "1":
            print(num_1, " + ", num_2, " = ", addition(num_1, num_2))

        elif user_choice == '2':
            print(num_1, " - ", num_2, " = ", subtraction(num_1, num_2))

        elif user_choice == '3':
            print(num_1, " * ", num_2, " = ", multiplication(num_1, num_2))
        elif user_choice == '4':
            print(num_1, " / ", num_2, " = ", division(num_1, num_2))

        #Asking user to continue or stop.
        next_operation = input("Do you want do the next operation? (yes/no):")
        if next_operation == "no":
            break
        else:
            print("This is an invalid input ")