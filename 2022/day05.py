from utils import file_to_list


def get_input(lines, crate_char_size=4):
    crate_idx = list(filter(lambda x: x.lstrip().startswith('1'), lines))[0].split(' ')
    crate_idx = list(filter(None, crate_idx))
    crates = {idx: [] for idx in crate_idx}
    instructions = []
    for line in lines:
        if line.lstrip().startswith('['):
            load_crates = [line[i:i+crate_char_size].strip() 
                           for i in range(0, len(line), crate_char_size)]
            for i, crate in enumerate(load_crates):
                if crate != '':
                    crates[str(i+1)].append(crate)
        if line.lstrip().startswith('move'):
            instruction = line.split(' ')
            instructions += [(instruction[1], instruction[3], instruction[5])]
    crates = {idx: crate[::-1] for idx, crate in crates.items()}
    return crate_idx, crates, instructions
            

def part1(lines):
    crate_idx, crates, instructions = get_input(lines)
    for num_moves, _from, _to in instructions:
        for _ in range(int(num_moves)):
            move_item = crates[_from].pop()
            crates[_to].append(move_item)
    return "".join((crates[idx][-1] for idx in crate_idx)).replace('[', '').replace(']', '')


def part2(lines):
    crate_idx, crates, instructions = get_input(lines)
    for num_moves, _from, _to in instructions:
        move_items = crates[_from][-int(num_moves):]
        crates[_from] = crates[_from][:-int(num_moves)]
        crates[_to] += move_items
    return "".join((crates[idx][-1] for idx in crate_idx)).replace('[', '').replace(']', '')


if __name__ == '__main__':
    lines = file_to_list('day05.txt', test=False, strip=False)
    lines = [line.replace('\n', '') for line in lines]
    
    result1 = part1(lines)
    print("Day 5, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 5, part 2:", result2)
