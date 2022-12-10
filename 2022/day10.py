from utils import file_to_list


def part1(lines):
    cycle = 1
    cycles = []
    x = 1
    for line in lines:
        if line[0] == 'noop': 
            cycle_num = 1
            cycle_cnt = 0
        else: 
            cycle_num = 2
            cycle_cnt = int(line[1])
        
        for i in range(cycle_num): 
            cycle += 1
            if i == (cycle_num-1):
                x += cycle_cnt
            if (cycle - 20) % 40 == 0:
                cycles.append((cycle, cycle*x))
    return cycles


def part2(lines):
    x, cycle = 1, 1
    cycles, sprites, sprite = [], [], []
    for line in lines:
        if line[0] == 'noop': 
            cycle_num = 1
            cycle_cnt = 0
        else: 
            cycle_num = 2
            cycle_cnt = int(line[1])
        
        for i in range(cycle_num): 
            if ((cycle % 40)-1) in (x-1, x, x+1):
                sprite.append('#')
            else:
                sprite.append('.')
            
            cycle += 1
            if ((cycle % 40)-1) == 0:
                sprites.append(sprite)
                print("".join(sprite))
                sprite = []
            
            if i == (cycle_num-1):
                x += cycle_cnt
            if (cycle - 20) % 40 == 0:
                cycles.append((cycle, cycle*x))
    return


if __name__ == '__main__':
    lines = file_to_list('day10.txt', test=False, cast=str.split)
    
    result1 = part1(lines)
    print("Day 10, part 1:", sum(c[1] for c in result1))
    
    print("Day 10, part 2:")
    part2(lines)
