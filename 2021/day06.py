from utils import file_to_list


class Lanternfish:
    internal_counter = -1
    new_cycle_timer = 6
    newborn_cycle_addition = 2
    
    def __init__(self, remaining_cycle_days):
        self.remaining_cycle_days = remaining_cycle_days
    
    def set_new_cycle(self):
        if self.remaining_cycle_days == 0:
            self.remaining_cycle_days = self.new_cycle_timer
        else:
            self.remaining_cycle_days += self.internal_counter
    
    def get_new_lanternfish(self):
        if self.remaining_cycle_days == 0:
            remaining_cycle_days = self.new_cycle_timer + self.newborn_cycle_addition
            return Lanternfish(remaining_cycle_days)

def get_initial_lanternfishes(lines):
    lanternfishes = []
    for remaining_cycle_days in lines:
        lanternfish = Lanternfish(remaining_cycle_days)
        lanternfishes.append(lanternfish)
    return lanternfishes

def part1(lines, days_to_run=80):
    lanternfishes = get_initial_lanternfishes(lines)
    for _ in range(days_to_run):
        new_lanternfishes = []
        for lanternfish in lanternfishes:
            new_lanternfish = lanternfish.get_new_lanternfish()
            new_lanternfishes.append(new_lanternfish)
            lanternfish.set_new_cycle()
        lanternfishes += list(filter(None, new_lanternfishes))
    return len(lanternfishes)
   
def part2(lines, days_to_run=256):
    total = len(lines)
    available_dict = {i: lines.count(i) for i in range(9)}
    for _ in range(days_to_run-1):
        available_dict[7] += available_dict[0]
        for key, value in list(available_dict.items()):
            if key == 0: key = 9
            available_dict[key-1] = value
        total += available_dict[0]
    return total
        
            
if __name__ == '__main__':
    lines = file_to_list('day06.txt', test=False, sep=',', cast=int)
    
    # result1 = part1(lines) - time expensive
    result1 = part2(lines, 80)
    print("Day 6, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 6, part 2:", result2)
    