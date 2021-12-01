from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def read_column(filename='day01.txt'):
    with open(BASE_DIR / filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return list(map(int, lines))

def get_lines():
    lines = read_column('day01.txt')
    lines = sorted(lines)
    return lines, reversed(lines)


def find_part1():
    lines, lines_reverse = get_lines()

    for r_line in lines_reverse:
        for line in lines:
            if line + r_line == 2020:
                return line, r_line
            if line + r_line > 2020:
                break

def find_part2():
    lines, _ = get_lines()

    for line1 in lines:
        for line2 in lines:
            if line1 + line2 > 2020:
                break
            for line3 in lines:
                if line1 + line2 + line3 > 2020:
                    break
                if line1 + line2 + line3 == 2020:
                    return line1, line2, line3

def part1():
    x, y = find_part1()
    return x * y

def part2():
    x, y, z = find_part2()
    return x * y * z

if __name__ == '__main__':
    result1 = part1()
    print("Day 1, part 1:", result1)

    result2 = part2()
    print("Day 1, part 2:", result2)
    