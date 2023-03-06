from datetime import date


class Person:
    def __init__(self, name: str, surname: str, year_of_birth: int):
        self._name = name
        self._surname = surname
        self.__year_of_birth = year_of_birth

    def print_full_name(self):
        print(f"{self._name} {self._surname}")

    def get_age(self) -> int:
        year_today = date.today().year  # 2022
        return year_today - self.__year_of_birth

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname


class Employee(Person):
    def __init__(self, name: str, surname: str, year_of_birth: int, type_of_employment: str):
        super().__init__(name, surname, year_of_birth)
        self.type_of_employment = type_of_employment

    def change_employment_type(self, new_type: str):
        self.type_of_employment = new_type


class Student(Person):
    def __init__(self, name: str, surname: str, year_of_birth: int, initial_grades=None):
        super().__init__(name, surname, year_of_birth)
        if initial_grades is None:
            initial_grades = []
        self.initial_grades = initial_grades

    def add_grade(self, grade: int):
        if not isinstance(grade, int):
            return False
        self.initial_grades.append(grade)
        return None

    def calculate_grade(self) -> float:
        grade = round(sum(self.initial_grades) / len(self.initial_grades))
        return grade

    def clear_list(self):
        self.initial_grades = []


if __name__ == "__main__":
    andrzej_programmer = Employee("Andrzej", "Programmer", 1999, "B2B")
    andrzej_programmer.print_full_name()

    stefan = Person("Stefan", "Testowy", 1999)
    stefan.print_full_name()
    print(stefan.get_age())
    # stefan.change_surname("Nietestowy")
    stefan.surname = "Nietestowy"

    stefan.print_full_name()
