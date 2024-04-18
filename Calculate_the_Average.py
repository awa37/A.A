def calculate_average(lst):
    # Get the sum of the list using the sum() function
    total = sum(lst)
    
    # Divide the sum by the length of the list to get the average
    average = total / len(lst)
    
    return average

# Example usage
numbers = [5, 10, 15, 20]
result = calculate_average(numbers)
print("The average of the numbers is:", result)

