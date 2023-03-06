with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = file.readlines()
    total = 0
    for number in numbers:
        total += int(number)

print(f"Sum of values equals {total}")
