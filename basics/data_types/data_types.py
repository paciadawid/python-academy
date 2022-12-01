a_int = 1  # -> integers, no max/min value

a_float = 1.0  # -> float definition

a_string = "test"  # string is list of chars, there is no char type
a_string2 = 'test'  # " and ' are the same
print(a_string[1])

a_list = [1, 1, 1.0, "1", [1, 2, 3]]  # mutable(can be edited), ordered, can be repeated
print(a_list[1])
a_list[3] = 2
a_list.append("test")
# a_list.remove("1")
del a_list[2]
print(a_list[-1])  # negative indexes
print(a_list[0:3])  # slicing

a_tuple = (0, 1, "2")  # not mutable, ordered, can be repeated
# a_tuple[0] = 1 -> throw exception

a_dict = {"title": "Harry potter", "author": "JK Rowling", "items": 2}  # mutable, not ordered, unique (keys)
a_dict2 = {"key": "value", 0: 1}  # int as key not recommended
print(a_dict["title"])
a_dict["items"] = 3
a_dict["cover"] = "hard"
print(a_dict)

a_set = {0, 2, 1, 2}  # collection of unique values (mutable, not ordered, unique)
print(a_set)

a_bool = ""

if a_bool:  # False for 0, "", [], (), {}, None
    print("This is true")
else:
    print("This is false")

a_none = None

pajton = {
    "animal_type": "cat",
    "age": 4,
    "weight": 4.5,
    "if_alive": True,
    "toys": ["mouse", "ball", "birds"],
    "colours": ("white", "grey", "black")
}

hobby = "sleeping"

print("I like " + hobby + " a lot")
print("I like {} a lot".format(hobby))  # interpolation
print(f"I like {hobby} a lot")  # f-strings

print("My " + pajton["animal_type"] + " has " + str(pajton["age"]) + " years")
print("My {} has {} years".format(pajton["animal_type"], pajton["age"]))
print(f"My {pajton['animal_type']} has {pajton['age']} years")
