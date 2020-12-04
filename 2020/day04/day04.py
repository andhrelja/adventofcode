from pathlib import Path
import re

# Incomplete

BASE_DIR = Path(__file__).resolve().parent
DELIMITER = '\n'
KEYS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]

VALIDATE = {
    'byr': lambda x: True if int(x) in range(1920, 2003) else False,
    'iyr': lambda x: True if int(x) in range(2010, 2021) else False,
    'eyr': lambda x: True if int(x) in range(2020, 2031) else False,
    'hgt': lambda x: True if int(x[:-2]) in range(150, 194) and x[-2:] == 'cm' \
                        else True if int(x[:2]) in range(59, 77) and x[2:] == 'in' \
                            else False,
    'hcl': lambda x: bool(re.match('^#([a-f]|[0-9])+', x)),
    'ecl': lambda x: True if x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') else False,
    'pid': lambda x: True if len(x) == 9 else False,
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

def part1(dictionary, validate=False):
    count_valid = 0
    for _, attrs in dictionary.items():
        input_keys = list(sorted(attrs.keys()))
        valid_keys = list(sorted(KEYS))
        if 'cid' not in input_keys:
            valid_keys.remove('cid')
        if not validate and input_keys == valid_keys:
            count_valid += 1
        elif validate:
            bools = list()
            for key, item in attrs.items():
                #print(key, item, VALIDATE[key](item))
                try:
                    bools.append(VALIDATE[key](item))
                except ValueError:
                    bools.append(False)
            if all(bools):
                count_valid += 1
    return count_valid


def part2(dictionary):
    return part1(dictionary, validate=True)


if __name__ == '__main__':
    input1 = read_input()
    cleaned_input = clean_input(input1)
    new_dictionary = remake_dictionary(cleaned_input)
    
    result1 = part1(new_dictionary)
    print("Day 4, part 1:", result1)

    result2 = part2(new_dictionary)
    print("Day 4, part 2:", result2)
