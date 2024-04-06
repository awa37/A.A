# Take input from the user for the number
number = int(input("Enter a number to calculate its factorial: "))

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a loop
for i in range(1, number + 1):
    factorial *= i

# Print the factorial
print("Factorial of", number, "is:", factorial)
9
