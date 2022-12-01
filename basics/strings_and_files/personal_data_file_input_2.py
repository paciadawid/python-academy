personal_dict = {}
people = []
# solutions 1
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if line == "\n":
        people.append(personal_dict)
        personal_dict = {}
    else:
        records = line.strip().split(" ")
        for record in records:
            key, value = record.split(":")
            personal_dict[key] = value
people.append(personal_dict)

print(people)
