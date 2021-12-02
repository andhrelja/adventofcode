from utils import file_to_list

switcher1 = {
    'forward': lambda x, y, value: (x + value, y),
    'down': lambda x, y, value: (x, y + value),
    'up': lambda x, y, value: (x, y - value)
}

switcher2 = {
    'forward': lambda x, y, aim, value: (x + value, y + (aim*value), aim),
    'down': lambda x, y, aim, value: (x, y, aim + value),
    'up': lambda x, y, aim, value: (x, y, aim - value)
}

def part1(lines):
    x, y = 0, 0
    for line in lines:
        direction, value = line.split(" ")
        value = int(value)
        fn = switcher1[direction]
        x, y = fn(x, y, value)
    return x*y

def part2(lines):
    x, y, aim = 0, 0, 0
    for line in lines:
        direction, value = line.split(" ")
        value = int(value)
        fn = switcher2[direction]
        x, y, aim = fn(x, y, aim, value)
    return x*y


if __name__ == '__main__':
    lines = file_to_list('day02.txt', test=False)
    
    result1 = part1(lines)
    print("Day 2, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 2, part 2:", result2)