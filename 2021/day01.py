from utils import file_to_list

def part1(lines):
    increases = 0
    previous = None
    
    for i, line in enumerate(lines[:-1]):
        previous = int(line)
        if int(lines[i+1]) > previous:
            increases += 1
        
    print("# of increases:", increases)

def part2(lines):
    outbound = []
    for i, line in enumerate(lines[:-2]):
        three_measures = [
            int(lines[i]),
            int(lines[i+1]),
            int(lines[i+2]),
        ]
        outbound.append(sum(three_measures))
    return outbound

if __name__ == '__main__':
    lines = file_to_list('day01.txt')
    print("Part 1:")
    part1(lines)
    print()
    print("Part 2:")
    new_lines = part2(lines)
    part1(new_lines)