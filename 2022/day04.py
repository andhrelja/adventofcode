from utils import file_to_list


def part1(lines):
    count = 0
    for p1, p2 in lines:
        p11, p12 = tuple(map(int, p1.split('-')))
        p21, p22 = tuple(map(int, p2.split('-')))
        r1, r2 = set(range(p11, p12+1)), set(range(p21, p22+1))
        count += r1.issuperset(r2) or r2.issuperset(r1)
    return count


def part2(lines):
    count = 0
    for p1, p2 in lines:
        p11, p12 = tuple(map(int, p1.split('-')))
        p21, p22 = tuple(map(int, p2.split('-')))
        r1, r2 = set(range(p11, p12+1)), set(range(p21, p22+1))
        count += 1 if r1.intersection(r2) else 0
    return count


if __name__ == '__main__':
    lines = file_to_list('day04.txt', test=False)
    lines = [line.split(',') for line in lines]
        
    result1 = part1(lines)
    print("Day 4, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 4, part 2:", result2)
