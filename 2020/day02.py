from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

cleaned = lambda x: [i.strip() for i in x]

def read_column(filename='day02.txt'):
    with open(BASE_DIR / filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines

def processed_lines(lines):
    processed = list()
    for line in lines:
        split_line = line.split(":")
        clean_line = cleaned(split_line)

        dirty_policy = clean_line[0]
        split_policy = dirty_policy.split(" ")

        policy = cleaned(split_policy)
        _min, _max = policy[0].split("-")
        char = policy[1]
        password = clean_line[1]
        processed.append({
            'min_occurance': int(_min),
            'max_occurance': int(_max),
            'char': char,
            'password': password,
        })
    return processed

def count_occurance(char, password):
    count = 0
    for chr in password:
        if chr == char:
            count += 1
    return count

def make_valid(processed_lines):
    for dictionary in processed_lines:
        occurances = count_occurance(dictionary['char'], dictionary['password'])
        if occurances in range(dictionary['min_occurance'], dictionary['max_occurance'] + 1):
            dictionary['valid'] = True
        else:
            dictionary['valid'] = False

def part1(processed_lines):
    valid_count = 0
    for dictionary in processed_lines:
        if dictionary['valid']:
            valid_count += 1
    return valid_count

def part2(processed_lines):
    valid_count = 0
    for dictionary in processed_lines:
        i1 = dictionary['min_occurance'] - 1
        i2 = dictionary['max_occurance'] - 1
        if dictionary['password'][i1] == dictionary['char'] and dictionary['password'][i2] != dictionary['char'] \
            or dictionary['password'][i1] != dictionary['char'] and dictionary['password'][i2] == dictionary['char']:
            valid_count += 1
    return valid_count

if __name__ == '__main__':
    lines = read_column()
    processed = processed_lines(lines)

    make_valid(processed)

    result1 = part1(processed)
    print("Day 2, part 1:", result1)

    result2 = part2(processed)
    print("Day 2, part 2:", result2)
    