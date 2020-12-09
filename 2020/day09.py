from utils import file_to_list
from itertools import combinations

GROUP_SIZE = 25

def get_preamble_sums(preamble):
    combination_sums = list()
    preamble_combinations = combinations(preamble, 2)
    for comb in preamble_combinations:
        combination_sums.append(sum(comb))
    return combination_sums

def item_invalid(item, preamble):
    group_sums = get_preamble_sums(preamble)
    if item not in group_sums:
        return item
    else:
        return None

def part1(lines):
    for i in range(GROUP_SIZE, len(lines), GROUP_SIZE):
        for j in range(i - GROUP_SIZE, i):
            preamble_slice_low = j
            preamble_slice_high = j + GROUP_SIZE
            current = preamble_slice_high

            preamble = lines[preamble_slice_low:preamble_slice_high]
            preamble_sums = get_preamble_sums(preamble)
            
            if lines[current] not in preamble_sums:
                return current, lines[current]
    return None

def part2(result1, lines):
    position, value = result1
    lines = lines[:position]

    for i in range(len(lines)):
        for j in range(i + 2, len(lines) + 1):
            suma = sum(lines[i:j])
            if suma > value:
                break
            if suma == value:
                return min(lines[i:j]), max(lines[i:j])


if __name__ == '__main__':
    lines = file_to_list("day09.txt", test=False, cast=int)

    result1 = part1(lines)
    print("Day 9, part 1:", result1[1])

    result2 = part2(result1, lines)
    print("Day 9, part 2:", sum(result2))