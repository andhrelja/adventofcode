def get_intcode():
    with open("day02.txt", "r") as f:
        return [int(x) for x in f.read().split(",")]

def process_intcode(numbers):
    for i in range(0, len(numbers) - 3, 4):
        first = numbers[i + 1]
        second = numbers[i + 2]
        index = numbers[i + 3]
        if numbers[i] == 1:
            numbers[index] = numbers[first] + numbers[second]
        elif numbers[i] == 2:
            numbers[index] = numbers[first] * numbers[second]
        else:
            break
    return numbers


def get_part1():
    numbers = get_intcode()
    numbers[1] = 12
    numbers[2] = 2
    return process_intcode(numbers)[0]


def get_part2():
    for i in range(100):
        for j in range(100):
            numbers = get_intcode()
            numbers[1] = i
            numbers[2] = j
            numbers = process_intcode(numbers)
            if numbers[0] == 19690720:
                return (i, j)


print("Part 1:", get_part1())
print("Part 2:", get_part2())