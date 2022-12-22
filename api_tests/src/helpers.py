from faker import Faker


def get_random_id(min_value, max_value):
    fake = Faker()
    random_int = fake.random_int(min_value, max_value)
    return random_int
