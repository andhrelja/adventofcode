def get_masses():
    with open("day01.txt", "r") as f:
        return [int(item) for item in f.readlines()]


def get_fuel(masses):
    for mass in masses:
        yield mass // 3 - 2


def get_fuel_module(fuel):
    while fuel > 0:
        fuel = fuel // 3 - 2
        if fuel <= 0:
            yield 0
        else:
            yield fuel


def get_part1():
    masses = get_masses()
    fuel_required = get_fuel(masses)
    return sum(fuel_required)


def get_part2():
    masses = get_masses()
    fuel_required = get_fuel(masses)

    suma = 0
    for fuel in list(fuel_required):
        suma += sum(get_fuel_module(fuel), fuel)
    return suma

print("Part 1:", get_part1())
print("Part 2:", get_part2())