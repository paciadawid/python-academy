text = "kajak"

unique_letters = []

for letter in text:
    if letter not in unique_letters:
        unique_letters.append(letter)

print(unique_letters)

# solution 1
letters_dict = {}

for letter in unique_letters:
    letters_dict[letter] = text.count(letter)

print(letters_dict)

# solution 2
letters_dict = {}

for letter in text:
    if letter not in letters_dict:
        letters_dict[letter] = 1
    else:
        letters_dict[letter] += 1

print(letters_dict)
