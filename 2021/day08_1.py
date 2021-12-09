# Part 1 completed only
from utils import file_to_list
import difflib
import copy

NUMBERS_ALIGNMENT1 = {
    1: [None, None, 'c', None, None, 'f', None],
    4: [None, 'b', 'c', 'd', None, 'f', None],
    7: ['a', None, 'c', None, None, 'f', None],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
}

NUMBERS_ALIGNMENT2 = {
    0: ['a', 'b', 'c', None, 'e', 'f', 'g'],
    1: [None, None, 'c', None, None, 'f', None],
    2: ['a', None, 'c', 'd', 'e', None, 'g'],
    3: ['a', None, 'c', 'd', None, 'f', 'g'],
    4: [None, 'b', 'c', 'd', None, 'f', None],
    5: ['a', 'b', None, 'd', None, 'f', 'g'],
    6: ['a', 'b', None, 'd', 'e', 'f', 'g'],
    7: ['a', None, 'c', None, None, 'f', None],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', None, 'f', 'g']
}


def get_deserialized_lines(lines):
    deserialized = []
    for line in lines:
        _in, _out = line.split("|")
        _in, _out = _in.strip(), _out.strip()
        deserialized.append({
            'input': _in.split(" "),
            'output': _out.split(" ")
        })
    return deserialized

def get_diff_chars(output, line):
    missing, existing = [], []
    if len(output) != len(line):
        return missing, existing
    for diff in difflib.ndiff(output, line):
        diff = diff.strip().split(" ")
        if '+' in diff:
            existing.append(diff[-1])
        if '-' in diff:
            missing.append(diff[-1])
    return missing, existing

def part1(lines):
    count_unique = 0
    for line in lines:
        for output in line['output']:
            for num in NUMBERS_ALIGNMENT1.keys():
                out = "".join(sorted(output))
                segment = "".join(list(filter(None, NUMBERS_ALIGNMENT1[num])))
                missing, existing = get_diff_chars(out, segment)
                for old, new in zip(missing, existing):
                    out = out.replace(old, new)
                out = "".join(sorted(out))
                if out == segment:
                    count_unique += 1
                    break
    return count_unique

def part2(lines):
    part2_output = ""
    for line in lines:
        new_numbers_alignment = copy.deepcopy(NUMBERS_ALIGNMENT2)
        for input_line in line['input'] + line['output']:
            segment_found = False
            for num in NUMBERS_ALIGNMENT1.keys():
                out = "".join(sorted(input_line))
                segment = "".join(list(filter(None, NUMBERS_ALIGNMENT1[num])))
                missing, existing = get_diff_chars(out, segment)
                for old, new in zip(missing, existing):
                    out = out.replace(old, new)
                out = "".join(sorted(out))
                
                if out == segment:
                    segment_found = True
                    break
            
            if segment_found:
                for new, old in zip(missing, existing):
                    for i, item in enumerate(NUMBERS_ALIGNMENT1[num]):
                        if item == old:
                            for key in new_numbers_alignment.keys():
                                if new_numbers_alignment[key][i] is not None:
                                    new_numbers_alignment[key][i] = new

                
        easy_numbers = NUMBERS_ALIGNMENT1.keys()
        hard_numbers = (num for num in NUMBERS_ALIGNMENT2.keys() if num not in easy_numbers)
        for easy_key in easy_numbers:
            for hard_key in hard_numbers:
                for i, item in enumerate(new_numbers_alignment[easy_key]):
                    if item is not None:
                        new_numbers_alignment[hard_key][i] = item
        print(new_numbers_alignment)
        for output in line['output']:
            for num in new_numbers_alignment.keys():
                out = "".join(sorted(output))
                segment = "".join(list(filter(None, new_numbers_alignment[num])))
                if out == segment:
                    print("out:", output)
                    print("segment:", segment)
                    print("segment num:", num)
                    part2_output += str(num)
                    break
    return part2_output

if __name__ == '__main__':
    lines = file_to_list('day08.txt', test=True)
    lines = get_deserialized_lines(lines)
    
    result1 = part1(lines)
    print("Day 8, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 8, part 2:", result2)
