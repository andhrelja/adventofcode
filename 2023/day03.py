from utils import file_to_list
import string
import numpy as np


diagonal_neighbours = lambda i, j, lines: [
    lines[i-1][j-1], # nw
    lines[i-1][j+1], # ne
    lines[i+1][j-1], # sw
    lines[i+1][j+1], # se
]

adjacent_neighbours = lambda i, j, lines: [
    lines[i][j-1], # n
    lines[i][j+1], # s
    lines[i-1][j], # w
    lines[i+1][j], # e
]


get_neighbours = lambda i, j, lines: [
    *_get_distinct_neighbours(lines[ i-1 ][ j-1 : j+2 ]),
    *_get_distinct_neighbours(lines[ i+1 ][ j-1 : j+2 ]),
    *_get_distinct_neighbours(lines[  i  ][ j+1 : j+2 ]),
    *_get_distinct_neighbours(lines[  i  ][ j-1 :  j  ]),
]

def _get_distinct_neighbours(neighbours):
    if not -1 in neighbours:
        return tuple(set(neighbours))
    
    l_n, r_n = set(), set()
    for i in neighbours:
        if i == -1:
            break
        if i > 0:
            l_n.add(i)
    for i in reversed(neighbours):
        if i == -1:
            break
        if i > 0:
            r_n.add(i)
    return (*l_n, *r_n)


def _stream_list(lst):
    yield from lst


def digits(stream):
    while digit := next(stream, 'abc') in string.digits:
        yield digit


def serialize_input(line):
    serialized_line = []
    number = ''
    endline = '\n'
    stream = _stream_list(line + endline)

    for char in stream:
        if not char.isdigit() and number:
            for _ in range(len(number)):
                serialized_line.append(int(number))
            number = ''
        
        if char == endline:
            continue

        if char.isdigit():
            number += char
            continue

        if char == '.':
            serialized_line.append(-1)
            continue
        else:
            serialized_line.append(0)
            continue
    
    return serialized_line


def apply_padding(lines):
    cols, rows = [-1], [-1] * (len(lines[0]) + 2)
    padded = [cols + lines[i] + cols 
              for i in range(len(lines))]
    padded = [rows] + padded + [rows]
    return padded


def part1(lines):
    summation = []
    d = False
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j] == 0:
                neighbours = (
                    *diagonal_neighbours(i, j, lines), 
                    *adjacent_neighbours(i, j, lines))

                # print('({}, {}): {}'.format(i, j, lines[i][j]))
                # print(neighbours)
                summation += list(filter(lambda x: x != -1, neighbours))
    return summation


def part2(lines):
    pass


if __name__ == '__main__':
    lines = file_to_list('day03.txt', test=True, _map=serialize_input)
    lines = apply_padding(list(lines))
    
    result1 = part1(lines)
    print("Day 3, part 1:", sum(result1))
    
    # result2 = part2(lines)
    # print("Day 3, part 2:", result2)
