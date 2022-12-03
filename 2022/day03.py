from utils import file_to_list


get_priority = lambda x: ord(x) - ord('a') + 1 if x.islower() \
    else ord(x) - ord('A') + 27


def get_intersect(main_item, *args):
    intersect = set(main_item).intersection(*args)
    assert len(intersect) == 1
    return intersect.pop()


def solve(rucksack_groups):
    for g_1, *g_n in rucksack_groups:
        yield get_priority(get_intersect(g_1, *g_n))


if __name__ == '__main__':
    assert get_priority('a') == 1
    assert get_priority('p') == 16
    assert get_priority('z') == 26
    assert get_priority('A') == 27
    assert get_priority('P') == 42
    assert get_priority('Z') == 52
    
    lines = file_to_list('day03.txt', test=False)
    
    part1 = [(line[:int(len(line) / 2)], line[int(len(line) / 2):]) for line in lines]
    result1 = sum(solve(part1))
    print("Day 3, part 1:", result1)
        
    group_size = 3
    part2 = [lines[i:i+group_size] for i in range(0, len(lines), group_size)]
    result2 = sum(solve(part2))
    print("Day 3, part 2:", result2)
