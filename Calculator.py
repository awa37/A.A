# Take input from the user for the first number
first_number = float(input("Enter the first number: "))

# Take input from the user for the second number
second_number = float(input("Enter the second number: "))

# Perform basic calculator functionalities
summation = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Check if the second number is not zero to avoid division by zero error
if second_number != 0:
    division = first_number / second_number
else:
    division = "Undefined (Division by zero)"

# Print the results
print("Sum:", summation)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

