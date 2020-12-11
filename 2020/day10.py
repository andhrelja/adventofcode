from utils import file_to_list

DIFFERENCES = {
    1: [],
    2: [],
    3: []
}

def part1(jolts, previous_jolt=0):
    for jolt in jolts:
        for diff in range(1, 4):
            if jolt - diff == previous_jolt:
                previous_jolt = jolt
                DIFFERENCES[diff].append(jolt)
    DIFFERENCES[3].append(max(jolts) + 3)

def get_initial_jolts(jolts):
    for i, jolt in enumerate(jolts[:3]):
        if jolt <= 3:
            yield i, jolt

def find_options(current_jolt, jolts, options=[]):
    if len(jolts) == 1:
        return options
    
    for i, jolt in enumerate(jolts):
        if jolt - current_jolt <= 3:
            options.append()
            options += find_options(jolt, jolts[i + 1: ], options)


def part2(jolts):
    arrangements = list()
    initial_jolts = get_initial_jolts(jolts)
    for start, initial_jolt in initial_jolts:
        options = find_options(initial_jolt, jolts[start + 1: ])
        arrangements.append(options)
    return arrangements


if __name__ == '__main__':
    lines = file_to_list("day10.txt", test=True, cast=int)
    lines = sorted(lines)

    part1(lines)
    result1 = len(DIFFERENCES[1]) * len(DIFFERENCES[3])
    print("Day 10, part 1:", result1)

    result2 = part2(lines)
    print("Day 10, part 2:", result2)
    