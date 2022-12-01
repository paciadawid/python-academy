pesel = "55030101193"
weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

length = len(weights)

sum = 0
for i in range(length):
    sum += int(pesel[i]) * weights[i]

checksum = 10 - sum % 10
print(checksum)
