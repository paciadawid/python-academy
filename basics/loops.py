for i in range(10):
    print(i)

fruits = ["apple", "banana", "error", "grape"]
name = "Ste7an"

for fruit in fruits:
    if fruit == "error":
        continue
    print(fruit)

for letter in name:
    if letter in "1234567890":  # equivalent to ["1", "2", "3", "4"...]
        print(f"{letter} is not a letter!")
        break
    print(letter)

a, b = 0, 10

while a < b:
    print(f"a={a}, b={b}")
    a += 1

for i in range(10, 100):
    if i % 2 == 0:
        print(i)

for i in range(10, 100, 2):
    print(i)

a = 10
while a < 100:
    print(a)
    a += 2
