isbn = "030640615"

total_sum = 0
for i, digit in enumerate(isbn):
    number = int(digit)
    total_sum += (i + 1) * number

checksum = total_sum % 11
print(f"Check number is {checksum}")
