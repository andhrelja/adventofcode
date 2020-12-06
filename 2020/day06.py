from itertools import count
from utils import file_to_list

# Incomplete

def part1(lines):
    sum_all = 0
    for group in lines:
        group = group.replace('\n', '')
        distinct_line = list(set(group))
        sum_all += len(distinct_line)
    return sum_all

def part2(lines):
    sum_all = 0
    for group in lines:
        members_answers = group.split('\n')
        members_num = len(members_answers)
        if members_num == 1:
            sum_all += len(members_answers[0])
        else:
            first_answer = members_answers[0]
            for char in first_answer:
                count_occurances = 1
                for answer in members_answers[1:]:
                    if char in answer:
                        count_occurances += 1
                if count_occurances == members_num:
                    sum_all += 1
    return sum_all


if __name__ == '__main__':
    lines = file_to_list('day06.txt', test=False, sep='\n\n')

    result1 = part1(lines)
    print("Day 6, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 6, part 2:", result2)
