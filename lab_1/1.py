# Constants
P_RAIN = 0.3
UTILITIES = {
    "house": {"rain": 2, "dry": 5},
    "forest": {"rain": 0, "dry": 10}
}

def expected_utility(location, rain_prob):
    rain_utility = UTILITIES[location]["rain"]
    dry_utility = UTILITIES[location]["dry"]
    return rain_prob * rain_utility + (1 - rain_prob) * dry_utility

def choose_best_location(rain_prob):
    house_utility = expected_utility("house", rain_prob)
    forest_utility = expected_utility("forest", rain_prob)

    print(f"House expected utility: {house_utility}")
    print(f"Forest expected utility: {forest_utility}")

    if forest_utility > house_utility:
        print("The forest is the better choice!")
    else:
        print("It's better to stay in the house.")

def main():
    choose_best_location(P_RAIN)

main()
