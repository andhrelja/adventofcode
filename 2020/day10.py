from utils import file_to_list

DIFFERENCES = {
    1: [],
    2: [],
    3: []
}

def part1(lines, previous_jolt=0):
    for jolt in lines:
        for diff in range(1, 4):
            if jolt - diff == previous_jolt:
                previous_jolt = jolt
                DIFFERENCES[diff].append(jolt)
    DIFFERENCES[3].append(max(lines) + 3)

def get_initial_arrangement(lines, previous_jolt=0):
    arrangement = list()
    for jolt in lines:
        for diff in range(1, 4):
            if jolt - diff == previous_jolt:
                arrangement.append(jolt)
                previous_jolt = jolt
    return arrangement

def get_initial_arrangements(lines):
    arrangements = list()
    for i, line in enumerate(lines):
        if line <= 3:
            initial_arrangement = get_initial_arrangement(lines[i:])
            arrangements.append(initial_arrangement)
    return arrangements

def find_options(item, arrangement):
    options = list()
    for i in range(1, 4):
        if item + i in arrangement:
            options.append(item + i)
    return options

def arrangement_exists(last_item, arrangements):
    existing_arrangements = list()
    for i, arrangement in enumerate(arrangements):
        last_index = len(arrangement) - 1
        if arrangement[last_index] == last_item:
            existing_arrangements.append(i)
    return existing_arrangements


def part2(lines):
    initial_arrangements = list()
    all_arrangements = list()
    
    initial_arrangements = get_initial_arrangements(lines)
    #print(initial_arrangements)
    for initial_arrangement in initial_arrangements:
        for i, item in enumerate(initial_arrangement[:-1]):
            options = find_options(item, lines[i:])
            # print("Current: {}\nOptions: {}".format(item, options))
            arrangement_indices = arrangement_exists(item, all_arrangements)
            if not arrangement_indices:
                all_arrangements.append([item])
                arrangement_indices = arrangement_exists(item, all_arrangements)
            
            existing_arrangements = list()
            for arrangement_index in sorted(arrangement_indices, reverse=True):
                existing_arrangements.append(all_arrangements.pop(arrangement_index))
            
            for option in options:
                for existing_arrangement in existing_arrangements:
                    all_arrangements.append(existing_arrangement + [option])
    
    # for initial_arrangement in initial_arrangements:
    #     all_arrangements.remove(initial_arrangement)
    return all_arrangements


if __name__ == '__main__':
    lines = file_to_list("day10.txt", test=False, cast=int)
    lines = sorted(lines)

    part1(lines)
    result1 = len(DIFFERENCES[1]) * len(DIFFERENCES[3])
    print("Day 10, part 1:", result1)

    import time

    start = time.time()
    result2 = part2(lines)
    print("Day 10, part 2:", len(result2))
    end = time.time()
    time_elapsed = "Time elapsed: {} min".format(((end - start) / 60))