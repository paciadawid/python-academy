import unittest

from basics.oop.person import Person, Student


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.stefan = Person("Stefan", "Testowy", 1999)

    def test_full_name(self):
        self.assertEqual(f"{self.stefan._name} {self.stefan.surname}", "Stefan Testowy")

    def test_change_name(self):
        self.stefan.surname = "Nietestowy"
        self.assertEqual("Nietestowy", self.stefan.surname)


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Nowy", "Student", 1999)

    def test_no_grades(self):
        self.assertFalse(self.student.initial_grades)

    def test_cleaning_list(self):
        self.student.add_grade(5)
        self.assertEqual(self.student.calculate_grade(), 5)
        self.student.clear_list()
        self.assertFalse(self.student.initial_grades)


if __name__ == "__main__":
    unittest.main()
