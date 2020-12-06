from utils import file_to_list

# Incomplete

def part1(lines):
    sum_all = 0
    for group in lines:
        group = group.replace('\n', '')
        distinct_line = list(set(group))
        sum_all += len(distinct_line)
    return sum_all

def count_occurances(string, char):
    count = 0
    for ch in string:
        if ch == char:
            count += 1
    return count

def part2(lines):
    sum_all = 0
    for group in lines:
        members_num = count_occurances(group, '\n')
        group = group.replace('\n', '')
        distinct_line = list(set(group))
        if len(distinct_line) < members_num:
            sum_all += len(distinct_line)
    return sum_all


if __name__ == '__main__':
    lines = file_to_list('day06.txt', test=True, sep='\n\n')

    result1 = part1(lines)
    print("Day 6, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 6, part 2:", result2)