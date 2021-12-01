from utils import file_to_list

def find_pos(line='FBFBBFF', i=0, lower=0, upper=127, chars=('F', 'B')):
    if i == len(line):
        return min(lower, upper)
    
    if line[i] == chars[0]:
        calc = upper - lower
        upper = lower + calc // 2
        return find_pos(line, i+1, lower, upper, chars)
    elif line[i] == chars[1]:
        calc = upper - lower
        lower = lower + (calc // 2) + 1
        return find_pos(line, i+1, lower, upper, chars)
    else:
        return None

def part1(lines):
    products = list()
    for line in lines:
        row_line = line[:7]
        seat_line = line[7:]

        row = find_pos(row_line, i=0, lower=0, upper=127, chars=('F', 'B'))
        seat = find_pos(seat_line, i=0, lower=0, upper=7, chars=('L', 'R'))
        
        products.append((row * 8) + seat)
    return sorted(products)

def part2(products):
    min_seat_id = 10 * 8 + 0
    max_seat_id = 114 * 8 + 7

    for i in range(min_seat_id, max_seat_id + 1):
        if i not in products:
            return i

if __name__ == '__main__':
    lines = file_to_list('day05.txt', test=False)

    result1 = part1(lines)
    print("Day 5, part 1:", max(result1))
    result2 = part2(result1)
    print("Day 5, part 2:", result2)