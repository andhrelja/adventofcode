from utils import file_to_list
import copy

get_adjacent_indices = lambda x, y: (
    (x, y-1), (x-1, y-1), 
    (x-1, y), (x-1, y+1),
    (x, y+1), (x+1, y+1),
    (x+1, y), (x+1, y-1)
)
get_positive_adjacent_indices = lambda x, y: ((i, j) for (i, j) in get_adjacent_indices(x, y) if i >= 0 and j >= 0)


def mark_adjacent(lines, i, j, glows):
    lines[i][j] = 0
    glows.append((i, j))
    for adj_i, adj_j in get_positive_adjacent_indices(i, j):
        try:
            lines[adj_i][adj_j]
        except IndexError:
            continue
    
        if lines[adj_i][adj_j] == 9:
            glows = mark_adjacent(lines, adj_i, adj_j, glows)
        elif lines[adj_i][adj_j] not in (9, 0) or (
            lines[adj_i][adj_j] == 0 and (adj_i, adj_j) not in glows
        ):
            lines[adj_i][adj_j] += 1
        
    return glows

def part1(lines, num_steps=100):
    glow_count = 0
    for _ in range(num_steps):
        glows = []        

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if (i, j) not in glows and char != 9:
                    lines[i][j] += 1
                elif char == 9:
                    glows = mark_adjacent(lines, i, j, glows)
        
        glow_count += len(glows)
    return glow_count

def part2(lines):
    step_num = 0
    while True:
        glows = []
        step_num += 1

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if (i, j) not in glows and char != 9:
                    lines[i][j] += 1
                elif char == 9:
                    glows = mark_adjacent(lines, i, j, glows)

        if sum(char for line in lines for char in line) == 0:
            return step_num
    

if __name__ == '__main__':
    lines = file_to_list('day11.txt', test=False)
    lines = [list(map(int, list(line))) for line in lines]
    
    
    result1 = part1(copy.deepcopy(lines))
    print("Day 11, part 1:", result1)
    
    result2 = part2(copy.deepcopy(lines))
    print("Day 11, part 2:", result2)
