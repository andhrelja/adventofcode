from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent
DELIMITER = '\n'
KEYS = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
)

VALIDATE = {
    'byr': lambda x: int(x) in range(1920, 2003),
    'iyr': lambda x: int(x) in range(2010, 2021),
    'eyr': lambda x: int(x) in range(2020, 2031),
    'hgt': lambda x: True if int(x[:-2]) in range(150, 194) and x[-2:] == 'cm' \
                        else True if int(x[:2]) in range(59, 77) and x[2:] == 'in' \
                            else False,
    'hcl': lambda x: bool(re.match('^#([a-f]|[0-9]){6}', x)),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: len(x) == 9,
    'cid': lambda x: True 
}

cleaned = lambda x: [i.strip() for i in x]

def read_input(filename="day04.txt"):
    with open(BASE_DIR / filename, 'r') as f:
        lines = f.readlines()
        return lines

def clean_input(lines):
    i = 0
    dictionary = dict()
    dictionary[i] = str()
    
    for line in lines:
        if line.startswith(DELIMITER):
            i += 1
            dictionary[i] = str()
        else:
            dictionary[i] += ' ' + line.replace('\n', ' ')
            dictionary[i] = dictionary[i].strip(' ')
    return dictionary

def remake_dictionary(cleaned_input):
    new_dictionary = dict()
    for key, item in cleaned_input.items():
        new_dictionary[key] = dict()
        new_items = item.split(' ')
        for new_item in new_items:
            key_item = new_item.split(':')
            new_dictionary[key].update({
                key_item[0] : key_item[1]
            })
    return new_dictionary

def part1(dictionary):
    count_valid = 0
    for _, attrs in dictionary.items():
        input_keys = list(sorted(attrs.keys()))
        valid_keys = list(sorted(KEYS))
        if 'cid' not in input_keys:
            valid_keys.remove('cid')
        if input_keys == valid_keys:
            count_valid += 1
    return count_valid


def part2(dictionary):
    count_valid = 0
    for _, attrs in dictionary.items():
        input_keys = list(sorted(attrs.keys()))
        valid_keys = list(sorted(KEYS))
        if 'cid' not in input_keys:
            valid_keys.remove('cid')
        if input_keys == valid_keys:
            bools = list()
            for key, item in attrs.items():
                if key == 'hgt' and not (item.endswith('cm') or item.endswith('in')):
                    bools.append(False)
                else:
                    bools.append(VALIDATE[key](item))
            if all(bools):
                count_valid += 1
    return count_valid


if __name__ == '__main__':
    input1 = read_input("day04.txt")
    cleaned_input = clean_input(input1)
    new_dictionary = remake_dictionary(cleaned_input)
    
    result1 = part1(new_dictionary)
    print("Day 4, part 1:", result1)

    result2 = part2(new_dictionary)
    print("Day 4, part 2:", result2)
