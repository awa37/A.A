
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Sample scenario
def main():
    # Create new students
    student1 = Student("Ahmed", 22)
    student2 = Student("jhon", 17)

    # Add grades for students
    student1.add_grade(85)
    student1.add_grade(90)
    student2.add_grade(75)
    student2.add_grade(80)

    # Display student information
    print("Student 1:")
    student1.display_info()
    print("Average Grade:", student1.calculate_average_grade())
    print()

    print("Student 2:")
    student2.display_info()
    print("Average Grade:", student2.calculate_average_grade())

if __name__ == "__main__":
    main()
