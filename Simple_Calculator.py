''' 
This code is a mini calculator with just 3 operations and only 2 inputs
it will calculate either +, - and x wih two numbers
it has defensive programming to prevent the program from crashing
it is then written to a file
'''
# operational error 
#only file - file exception try /except
#zero division error - try/except filename = "equations.txt"

filename = "equations.txt"

while True:
    try:
        # User prompted input and only numerical values allowed
        #  otherwise re-prompted using while true/except value error
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # User prompted to choose an operation
        # while true used to only accept operation and re-prompted
        while True:
            op = input("Enter an operation (+, -, x): ")

            # Check if the operation is valid
            if op not in ["+", "-", "x"]:
                print("Invalid operation.")
            else:
                break

        # Perform the calculation
        # if statements to determine output of calculation 
        try:
            if op == "+":
                result = num1 + num2
                equation = f"{num1} + {num2} = {result}\n"
            elif op == "-":
                result = num1 - num2
                equation = f"{num1} - {num2} = {result}\n"
            elif op == "x":
                result = num1 * num2
                equation = f"{num1} x {num2} = {result}\n"
        except ZeroDivisionError:
            print("Error: Division by zero not allowed")
            continue

        # Write the equation to the file
        with open(filename, "a") as f:
            f.write(equation)

        # Display the calculation
        print(f"The result is: {result}")

        # Ask user if they want to do another equation or read out equations from a file
        while True:
            choice = input("Do you want to do another equation (y/n) or read out equations from a file (f)? ")

            if choice not in ["y", "n", "f"]:
                print("Invalid input. Please enter 'y', 'n', or 'f'.")
            else:
                break

        # If user wants to read out equations from a file
        if choice == "f":
            while True:
                filename = input("Enter filename: ")
                if filename.endswith(".txt"):
                    break
                else:
                    print("Invalid filename. Please enter a .txt file.")

            try:
                with open(filename, "r") as f:
                    for line in f:
                        print(line.strip())

            except FileNotFoundError:
                print("File not found. Please try again.")
                continue

        # If user enters anything else or wants to do another equation, continue loop
        if choice != "f":
            continue

        # If user enters "n", break loop
        else:
            break

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()


        