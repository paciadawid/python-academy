personal_dict = {}

# solutions 1
with open("personal.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        records = line.split(" ")

        for record in records:
            key, value = record.split(":")
            personal_dict[key] = value

# solution 2
with open("personal.txt", "r") as f:
    lines = f.readlines()
    records = []
    for line in lines:
        records.extend(line.split(" "))

for record in records:
    key, value = record.split(":")
    personal_dict[key] = value


print(personal_dict)
