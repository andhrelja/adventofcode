from utils import file_to_list


def part1(lines):
    min_pos, max_pos = min(lines), max(lines)
    
    min_fuel_consumption = abs(sum(lines) - min_pos)
    for pos in range(min_pos, max_pos):
        total_fuel_consumption = 0
        for key in lines:
            total_fuel_consumption += abs(key - pos)
        if total_fuel_consumption < min_fuel_consumption:
            min_fuel_consumption = total_fuel_consumption
    return min_fuel_consumption

def part2(lines):
    min_pos, max_pos = min(lines), max(lines)
        
    min_fuel_consumption = 999**9
    for pos in range(min_pos, max_pos):
        total_fuel_consumption = 0
        for key in lines:
            for i in range(abs(key - pos)):
                total_fuel_consumption += i+1
        if total_fuel_consumption < min_fuel_consumption:
            min_fuel_consumption = total_fuel_consumption
    return min_fuel_consumption

if __name__ == '__main__':
    lines = file_to_list('day07.txt', test=False, sep=',', cast=int)
    
    result1 = part1(lines)
    print("Day 7, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 7, part 2:", result2)