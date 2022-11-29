personal_data = "hcl:5d90f0 cid:270"

records = personal_data.split()

data_dict = {}
for record in records:
    key, value = record.split(":")
    data_dict[key] = value

print(data_dict)
