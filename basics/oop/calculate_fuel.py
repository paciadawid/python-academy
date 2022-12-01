def calculate_fuel(mass):
    fuel = mass // 3 - 2
    # fuel = int(mass / 3) - 2
    # fuel = math.floor(mass / 3) - 2

    return fuel


print(calculate_fuel(14))
