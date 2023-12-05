from utils import file_to_list

def serialize_input(line):
    card_sep_loc = line.find(':')
    card_name = line[:card_sep_loc]
    winning_numbers, owning_numbers = line[card_sep_loc+1:].split('|')
    winning_numbers = list(map(int, winning_numbers.strip().split()))
    owning_numbers = list(map(int, owning_numbers.strip().split()))
    return dict(
        card_name=card_name, 
        winning_numbers=winning_numbers, 
        owning_numbers=owning_numbers)



def part1(lines):
    summation = 0
    for item in lines:
        points = 0
        intersect = set(item['winning_numbers']).intersection(item['owning_numbers'])
        if len(intersect) == 1:
            points = 1
        if len(intersect) > 1:
            points = 2 ** (len(intersect) - 1)
        summation += points
    return summation


def part2(lines):
    return 0



if __name__ == '__main__':
    lines = file_to_list('day04.txt', test=False, _map=serialize_input)
    lines = list(lines)
        
    result1 = part1(lines)
    print("Day 4, part 1:", result1)
    
    # result2 = part2(lines)
    # print("Day 2, part 2:", result2)
