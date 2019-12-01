with open("day01.txt", "r") as f:
    masses = [int(item) for item in f.readlines()]

def get_fuel(masses):
    for mass in masses:
        yield int(mass / 3) - 2


if __name__ == '__main__':
    fuel_required = get_fuel(masses)
    print(sum(fuel_required))
