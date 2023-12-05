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

padding = 1
get_neighbours = lambda i, j, lines: [
    *get_distinct_neighbours(lines[ i-1 ][ j-1 : j+2 ]), # nw, n, ne
    *get_distinct_neighbours(lines[ i+1 ][ j-1 : j+2 ]), # sw, s, se
    *get_distinct_neighbours(lines[  i  ][ j+1 : j+2 ] + [-1]), # e
    *get_distinct_neighbours(lines[  i  ][ j-1 :  j  ] + [-1]), # w
]

def get_distinct_neighbours(neighbours):
    if neighbours[1] == -1:
        return (*list(neighbours),)
    return (*set(neighbours),)


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
    cols, rows = [-1], [-1] * (len(lines[0]) + padding * 2)
    padded = [(cols * padding) + lines[i] + (cols * padding)
              for i in range(len(lines))]
    padded = ([rows] * padding) + padded + ([rows] * padding)
    return padded


def part1(lines):
    summation = []
    for i in range(padding, len(lines) - padding):
        for j in range(padding, len(lines[i]) - padding):
            if lines[i][j] == 0:
                neighbours = list(
                    filter(lambda x: x != -1, 
                           get_neighbours(i, j, lines)))
                summation += neighbours
    return summation


def part2(lines):
    summation = 0
    for i in range(padding, len(lines) - padding):
        for j in range(padding, len(lines[i]) - padding):
            if lines[i][j] == 0:
                neighbours = list(
                    filter(lambda x: x != -1, 
                           get_neighbours(i, j, lines)))
                if len(neighbours) == 2:
                    summation += np.prod(neighbours)
    return summation


if __name__ == '__main__':
    lines = file_to_list('day03.txt', test=False, _map=serialize_input)
    lines = apply_padding(list(lines))
    
    result1 = part1(lines)
    print("Day 3, part 1:", sum(result1))
    
    result2 = part2(lines)
    print("Day 3, part 2:", result2)
