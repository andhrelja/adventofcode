from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

cleaned = lambda x: [i.strip() for i in x]

def read_input(filename="day03.txt"):
    with open(BASE_DIR / filename, 'r') as f:
        lines = f.readlines()
        return cleaned(lines)

def part1(right, down, cleaned_lines):
    r, d = 0, down
    trees_count = 0
    while d < len(cleaned_lines):
        r += right
        coeff = r / len(cleaned_lines[d])
        if coeff >= 1:
            cleaned_lines[d] += cleaned_lines[d]*int(coeff)

        if cleaned_lines[d][r] == '#':
            trees_count += 1
            
        d += down
    return trees_count

def part2(cleaned_lines):
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )
    multiply = 1
    for slope in slopes:
        count = part1(slope[0], slope[1], cleaned_lines)
        multiply *= count
    return multiply


if __name__ == '__main__':
    cleaned_lines = read_input()
    
    result1 = part1(3, 1, cleaned_lines)
    print("Day 3, part 1:", result1)

    result2 = part2(cleaned_lines)
    print("Day 3, part 2:", result2)