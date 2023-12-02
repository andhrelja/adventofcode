from utils import file_to_list
import string

digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def _update_digit_map():
    global digit_map
    add_digit_map = {}
    for key_a in digit_map:
        for key_b in digit_map:
            if key_a[-1] == key_b[0]:
                new_key = key_a + key_b[1:]
                new_val = digit_map[key_a] + digit_map[key_b]
                add_digit_map.update({
                    new_key: new_val 
                })
    add_digit_map.update(digit_map)
    digit_map = add_digit_map


def str_replace(x):
    for char in string.ascii_lowercase:
        x = x.replace(char, '')
    return x


def digit_replace(x):
    for digit_char, digit_num in digit_map.items():
        x = x.replace(digit_char, digit_num)
    return str_replace(x)


def part1(lines):
    lines = map(str_replace, lines)
    summation = []
    for line in lines:
        first, last = line[0], line[-1]
        summation.append(int(first + last))
    return sum(summation)


def part2(lines):
    _update_digit_map()
    lines = map(digit_replace, lines)
    summation = []
    for line in lines:
        first, last = line[0], line[-1]
        summation.append(int(first + last))
    return sum(summation)


if __name__ == '__main__':
    lines = file_to_list('day01-1.txt', test=False)
        
    result1 = part1(lines)
    print("Day 1, part 1:", result1)
    
    lines = file_to_list('day01-2.txt', test=False) 
    result2 = part2(lines)
    print("Day 1, part 2:", result2)
