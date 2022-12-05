from datetime import date


class Person:

    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self._surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_age(self):
        year_today = date.today().year  # 2022
        return year_today - self.year_of_birth

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname


stefan = Person("Stefan", "Testowy", 1999)
print(stefan.surname)
stefan.surname = "Nowe"
stefan.print_full_name()
