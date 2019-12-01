from day01 import masses, get_fuel

def get_fuel_module(fuel):
    res = fuel
    while res > 0:
        res = int(res / 3) - 2
        if res <= 0:
            yield 0
        else:
            yield res

def fuel_module():
    for fuel in list(get_fuel(masses)):
        yield sum(get_fuel_module(fuel), fuel)

print(sum(fuel_module()))