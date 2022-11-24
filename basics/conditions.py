destination = "Nicosia"

destinations_dict = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": None,
    "Gdansk": 485
}

distance = destinations_dict[destination]

if distance:

    cost = distance * 2

    if distance < 2000:
        cost += 100  # equivalent to cost = cost + 100

    print(f"Total cost to {destination} is {cost}")
else:
    print(f"There is no trip to {destination}")
