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


stefan = Person("Stefan", "Testowy", 1999)
stefan.print_full_name()
print(stefan.get_age())
stefan.change_surname("Nietestowy")
stefan.print_full_name()
