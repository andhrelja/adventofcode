from utils import file_to_list
import numpy as np

get_edges = lambda lines: (
    lines[0, :], lines[len(lines)-1, :],
    lines[:, 0], lines[:, len(lines[0])-1]
)

get_surrounding = lambda i, j, lines: [
    lines[:i, j][::-1],
    lines[i, :j][::-1],
    lines[i+1:, j],
    lines[i, j+1:]
]

get_adjecent = lambda i, j, lines: [
    lines[i, j-1],
    lines[i-1, j],
    lines[i, j+1],
    lines[i+1, j] 
]

def part1(lines):
    edges = get_edges(lines)
    visible = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            surrounding = get_surrounding(i, j, lines)
            adjacent = get_adjecent(i, j, lines)
            visible += any(adj < lines[i, j] 
                           for adj in adjacent) \
                       and any(
                           all(sur < lines[i, j] for sur in surr) 
                           for surr in surrounding)
    return (len(edges) * len(edges[0])) - 4 + visible


def part2(lines):
    all_scores = []
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            surrounding = get_surrounding(i, j, lines)
            scores = []
            for surr in surrounding:
                score = 0
                for sur in surr:
                    score += 1
                    if sur >= lines[i, j]:
                        break
                if score > 0:
                    scores.append(score)
            all_scores.append(((i,j), np.prod(scores)))
    return max(all_scores, key=lambda x: x[1])


if __name__ == '__main__':
    lines = file_to_list('day08.txt', test=False)
    lines = np.array([list(map(int, (c for c in line))) for line in lines])
    
    result1 = part1(lines)
    print("Day 8, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 8, part 2:", result2[1])
