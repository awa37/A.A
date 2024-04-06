
# Take input from the user for the upper limit
N = int(input("Enter a number (N): "))

# Loop through numbers from 2 to N
for num in range(2, N + 1):
    is_prime = True
    # Check if the number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # Print the prime number
    if is_prime:
        print(num)
