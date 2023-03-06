pesel = "55030101193"
weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

length = len(weights)

aggregator = 0
for i in range(length):
    aggregator += int(pesel[i]) * weights[i]

checksum = 10 - aggregator % 10
print(checksum)
