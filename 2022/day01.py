from utils import file_to_list


def get_sorted_calory_loads(lines):
    elf_calory_load = {}
    for i, elf_calory in enumerate(lines):
        elf_calories = list(map(int, elf_calory.split('\n')))
        elf_calory_load[i] = sum(elf_calories)
    return sorted(elf_calory_load.items(), key=lambda x: x[1])


def part1(lines):
    sorted_calory_loads = get_sorted_calory_loads(lines)
    return sum(dict(sorted_calory_loads[-1:]).values())


def part2(lines):
    sorted_calory_loads = get_sorted_calory_loads(lines)
    return sum(dict(sorted_calory_loads[-3:]).values())


if __name__ == '__main__':
    lines = file_to_list('day01.txt', test=False, sep='\n\n')
        
    result1 = part1(lines)
    print("Day 1, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 1, part 2:", result2)
