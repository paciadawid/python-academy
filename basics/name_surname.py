text = "andrzej testowy"

names = text.split()

name = names[0].capitalize()
surname = names[1].capitalize()

print(name, surname)

number_of_vowels = 0
for letter in text:
    if letter in "aeiouy":  # same as ["a", "e", "i", "o", "u", "y"]
        number_of_vowels += 1

print(number_of_vowels)
