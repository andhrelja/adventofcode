from utils import file_to_list
from collections import Counter
import numpy as np

DEFAULT_ALIGNMENT = 'abcdefg'
NUMBERS_ALIGNMENT = {
    0: ['a', 'b', 'c', None, 'e', 'f', 'g'],
    1: [None, None, 'c', None, None, 'f', None],
    2: ['a', None, 'c', 'd', 'e', None, 'g'],
    3: ['a', None, 'c', 'd', None, 'f', 'g'],
    4: [None, 'b', 'c', 'd', None, 'f', None],
    5: ['a', 'b', None, 'd', None, 'f', 'g'],
    6: ['a', 'b', None, 'd', 'e', 'f', 'g'],
    7: ['a', None, 'c', None, None, 'f', None],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', None, 'f', 'g'],
}

get_serialized_alignment = lambda alignment, num: "".join(list(filter(None, alignment[num])))
get_serialized1_alignment = lambda alignment, num: "".join([char if char is not None else "_" for char in alignment[num]])


def get_deserialized_lines(lines: list):
    deserialized = []
    for line in lines:
        _in, _out = line.split("|")
        _in, _out = _in.strip(), _out.strip()
        deserialized.append({
            'input': _in.split(" "),
            'output': _out.split(" ")
        })
    return deserialized

def _get_most_common_char(new_number_alignments: list):
    most_common_chars = []
    #print(num)
    new_number_alignments = np.transpose(np.array(new_number_alignments))
    #print(new_number_alignments)
    for i, align in enumerate(new_number_alignments):
        alignment_counter = Counter(list(filter(None, align))).most_common()
        if alignment_counter:
            most_common_chars.append(alignment_counter[0][0])
        else:
            most_common_chars.append(None)
        #print(i, alignment_counter)
    return np.transpose(np.array(most_common_chars))
    

def _get_new_number_alignment(digit: str, number: int):
    new_number_alignment = NUMBERS_ALIGNMENT[number]
    j = -1
    for char in digit:
        if char != NUMBERS_ALIGNMENT[number]:
            if new_number_alignment[j] is not None:
                j += 1
            while new_number_alignment[j] is None and j < len(NUMBERS_ALIGNMENT) - 1:
                j += 1
            new_number_alignment[j] = char
    return new_number_alignment
            

def part1(lines: list):
    easy_keys = (1, 4, 7, 8)
    number_allignments = []
    for item in lines:
        for digit in item['output']:
            for number in easy_keys:
                number_alignment = get_serialized_alignment(NUMBERS_ALIGNMENT, number)
                if len(number_alignment) == len(digit):
                    number_alignment = _get_new_number_alignment(digit, number)
                    number_allignments.append(number_alignment)
    return len(number_allignments)

def part2(lines: list):
    easy_keys = (1, 4, 7, 8)
    for item in lines:
        new_number_alignments = {}
        for digit in item['input']:
            for number in easy_keys:
                number_alignment = get_serialized_alignment(NUMBERS_ALIGNMENT, number)
                if len(number_alignment) == len(digit):
                    number_alignment = _get_new_number_alignment(digit, number)
                    new_number_alignments[number] = number_alignment
        
        search_most_common = [
            new_number_alignments[1],
            new_number_alignments[4],
            new_number_alignments[7]
        ]
        most_common_chars = _get_most_common_char(search_most_common)
        most_common_chars[4] = new_number_alignments[8][4]
        most_common_chars[6] = new_number_alignments[8][6]
        print(most_common_chars)
        
        for num in NUMBERS_ALIGNMENT.keys():
            if num != 8 and num in new_number_alignments.keys():                
                alignment = get_serialized_alignment(new_number_alignments, num)
                alignment1 = get_serialized1_alignment(new_number_alignments, num)
            else:
                most_common_chars = NUMBERS_ALIGNMENT[num]
                alignment = get_serialized_alignment(NUMBERS_ALIGNMENT, num)
                alignment1 = get_serialized1_alignment(NUMBERS_ALIGNMENT, num)
            #print(num, alignment1, len(alignment))
            
        #print(new_number_alignments, end="\n\n")
        print()
    return #new_number_alignments

if __name__ == '__main__':
    lines = file_to_list('day08.txt', test=True)
    lines = get_deserialized_lines(lines)
    
    result1 = part2(lines)
    print("Day 8, part 1:", result1)
    
    #result2 = part2(lines)
    #print("Day 8, part 2:", result2)