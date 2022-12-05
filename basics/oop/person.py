from datetime import date


class Person:

    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_age(self):
        year_today = date.today().year  # 2022
        return year_today - self.year_of_birth

    def change_surname(self, surname):
        self.surname = surname


class Employee(Person):

    def __init__(self, name, surname, year_of_birth, type_of_employment):
        super().__init__(name, surname, year_of_birth)
        self.type_of_employment = type_of_employment

    def change_employment_type(self, new_type):
        self.type_of_employment = new_type


class Student(Person):

    def __init__(self, name, surname, year_of_birth, initial_grades=None):
        super().__init__(name, surname, year_of_birth)
        if initial_grades is None:
            initial_grades = []
        self.initial_grades = initial_grades

    def add_grade(self, grade):
        self.initial_grades.append(grade)

    def calculate_grade(self):
        grade = round(sum(self.initial_grades) / len(self.initial_grades))
        return grade


if __name__ == "__main__":
    andrzej_programmer = Employee("Andrzej", "Programmer", 1999, "B2B")
    andrzej_programmer.print_full_name()

    stefan = Person("Stefan", "Testowy", 1999)
    stefan.print_full_name()
    print(stefan.get_age())
    stefan.change_surname("Nietestowy")
    stefan.print_full_name()
