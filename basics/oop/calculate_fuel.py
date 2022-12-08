def calculate_fuel(mass):
    if type(mass) not in [int, float]:
        return False
    if mass <= 0:
        return False
    fuel = mass // 3 - 2
    if mass < 9:
        return 1
    return fuel
