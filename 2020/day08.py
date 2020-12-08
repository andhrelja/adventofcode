from utils import file_to_list

def process_lines(lines):
    out = list()
    for line in lines:
        split_line = line.split(' ')
        operation = split_line[0].strip()
        argument = split_line[1].strip()
        out.append([operation, int(argument)])
    return out


def part1(lines):
    accumulator = 0
    visited = list()
    i = 0
    while i < len(lines):
        if i in visited:
            return accumulator
        visited.append(i)

        if lines[i][0] == 'nop':
            i += 1
        elif lines[i][0] == 'jmp':
            i += lines[i][1]
        elif lines[i][0] == 'acc':
            accumulator += lines[i][1]
            i += 1

def part2(lines, replaced=[]):
    accumulator = 0
    visited = list()
    i = 0
    while i <= len(lines):
        if i in visited:
            for j in reversed(visited):
                if j not in replaced and (lines[j][0] == 'nop' or lines[j][0] == 'jmp'):
                    lines1 = lines
                    replaced.append(j)
                    if lines[j][0] == 'nop':
                        lines1[j][0] = 'jmp'
                    elif lines[j][0] == 'jmp':
                        lines1[j][0] = 'nop'
                    return part2(lines1, replaced)
                    
        if i == len(lines):
            return accumulator
        visited.append(i)

        if lines[i][0] == 'nop':
            i += 1
        elif lines[i][0] == 'jmp':
            i += lines[i][1]
        elif lines[i][0] == 'acc':
            accumulator += lines[i][1]
            i += 1

if __name__ == '__main__':
    lines = file_to_list('day08.txt', test=False)
    lines = process_lines(lines)

    result1 = part1(lines)
    print("Day 8, part 1:", result1)

    result2 = part2(lines)
    print("Day 8, part 2:", result2)