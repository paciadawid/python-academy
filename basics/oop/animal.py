class Animal:

    def __init__(self, animal_type):
        self.animal_type = animal_type

    def make_a_sound(self):
        if self.animal_type == "cat":
            print("meow")
        elif self.animal_type == "dog":
            print("woof")
        else:
            print("no animal found")

    def calculate_food(self, weight):
        food = weight / 50
        return food


my_animal = Animal("cat")
my_animal.make_a_sound()
