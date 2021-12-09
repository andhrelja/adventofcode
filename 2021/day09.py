from utils import file_to_list
import numpy as np

get_adjacent_indices = lambda x, y: ((x, y-1), (x-1, y), (x, y+1), (x+1, y))
get_positive_adjacent_indices = lambda x, y: ((i, j) for (i, j) in get_adjacent_indices(x, y) if i >= 0 and j >= 0)

def part1(lines):
    low_points = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            char = int(char)
            adj_chars = []

            for adj_i, adj_j in get_positive_adjacent_indices(i, j):
                try:
                    adj_char = int(lines[adj_i][adj_j])
                except IndexError:
                    continue
                adj_chars.append(adj_char)
            
            if all(char < adj_char for adj_char in adj_chars):
                low_points.append((i, j))
    risk_level = sum((int(lines[i][j])+1 for (i, j) in low_points))
    return risk_level, low_points

def get_basin(i, j, lines, adj_chars, visited):
    for adj_i, adj_j in get_positive_adjacent_indices(i, j):
        try:
            adj_char = int(lines[adj_i][adj_j])
        except IndexError:
            continue
        
        if (adj_i, adj_j) not in visited and adj_char < 9:
            visited.append((adj_i, adj_j))
            adj_chars.append(adj_char)
            adj_chars = get_basin(adj_i, adj_j, lines, adj_chars, visited)

    return adj_chars
    
def part2(lines, low_points):
    basins = []
    for (x, y) in low_points:
        basin = get_basin(x, y, lines, [int(lines[x][y])], [(x, y)])
        basins.append(len(basin))
    basins = sorted(basins)
    return np.prod(basins[-3:])

if __name__ == '__main__':
    lines = file_to_list('day09.txt', test=False)
    
    result1, low_points = part1(lines)
    print("Day 9, part 1:", result1)
    
    result2 = part2(lines, low_points)
    print("Day 9, part 2:", result2)
