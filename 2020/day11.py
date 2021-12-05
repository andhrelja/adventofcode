from utils import file_to_list
import copy

get_deserialized_lines = lambda lines: [list(line) for line in lines]
get_adjacent_seats = lambda i, j: ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1))
switcher = {
    'L': False,
    '#': True,
    '.': None
}

def get_adjacent_seats2(i, j, len_x, len_y):
    adjacent_seats = set()

    # North - South
    north_south = set()
    for ix in range(0, len_x):
        north_south.add((ix, j))
    # East - West
    east_west = set()
    for jy in range(0, len_y):
        east_west.add((i, jy))
    
    # Northeast - Southwest
    northeast_southwest = set()
    for ix in range(0, len_x):
        if ix <= i:
            if i-ix >= 0 and i-ix < len_x and j-ix < len_x:
                northeast_southwest.add((i-ix, j-ix))
        else:
            if i+(ix-i) >= 0 and i+(ix-i) < len_x and j+(ix-j) < len_x:
                northeast_southwest.add((i+(ix-i), j+(ix-j)))

    # Northwest - Southeast
    northwest_southeast = set()
    for jy in range(0, len_y):
        if jy <= j:
            if i-jy >= 0 and i-jy < len_x and j+jy < len_y:
                northwest_southeast.add((i-jy, j+jy))
        else:
            if i+(jy-i) >= 0 and i+(jy-i) < len_x and j-(jy-j) < len_y:
                northwest_southeast.add((i+(jy-i), j-(jy-j)))
    adjacent_seats = north_south.union(
        east_west.union(
            northeast_southwest.union(
                northwest_southeast
            )
        )
    )
    adjacent_seats.remove((i, j))
    return adjacent_seats

def print_adjacent(adjacent_seats, len_x, len_y):
    _list = []
    for i in range(len_x):
        inner = []
        for j in range(len_y):
            inner.append('.')
        _list.append(inner)
    for i, j in adjacent_seats:
        _list[i][j] = '#'
    
    for item in _list:
        print("".join(item))

def get_part1_solution(lines):
    occupied_count = 0
    for line in lines:
        occupied_count += line.count('#')
    return occupied_count

def part1(lines):
    new_lines = copy.deepcopy(lines)
    for i, line in enumerate(lines):
        for j, seat in enumerate(line):
            if seat == 'L':
                adj_seats = set()
                for adj_i, adj_j in get_adjacent_seats(i, j):
                    if adj_i >= 0 and adj_j >= 0:
                        try:
                            is_seat_occupied = switcher[lines[adj_i][adj_j]]
                        except IndexError:
                            is_seat_occupied = None
                        
                        if is_seat_occupied is not None:
                            adj_seats.add(is_seat_occupied)

                if adj_seats == set([False]):
                    new_lines[i][j] = '#'
                
            elif seat == '#':
                adj_seats_occupied = 0
                for adj_i, adj_j in get_adjacent_seats(i, j):
                    if adj_i >= 0 and adj_j >= 0:
                        try:
                            is_seat_occupied = switcher[lines[adj_i][adj_j]]
                        except IndexError:
                            is_seat_occupied = None

                        if is_seat_occupied == True:
                            adj_seats_occupied += 1
                    
                if adj_seats_occupied >= 4:
                    new_lines[i][j] = 'L'

    if lines == new_lines:
        return get_part1_solution(new_lines)
    else:
        return part1(new_lines)


if __name__ == '__main__':
    lines = file_to_list('day11.txt', test=False)
    lines = get_deserialized_lines(lines)
    
    #result1 = part1(lines)
    #print("Day 11, part 1:", result1)
    
    adj_seats = get_adjacent_seats2(2, 3, 5, 6)
    print_adjacent(adj_seats, 5, 6)