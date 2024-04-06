
def calculate_age(start_year, end_year):
    return end_year - start_year

def main():
    start_year = int(input("Enter the year the person was born or the item was created: "))
    end_year = int(input("Enter the current year: "))

    age = calculate_age(start_year, end_year)

    print("The age is:", age)

if __name__ == "__main__":
    main()
    