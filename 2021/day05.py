from utils import file_to_list
import numpy as np


def get_deserialized_lines(lines):
    max_axis = 0
    deserialized = []
    for line in lines:
        new_line = line.split(' -> ')
        _from = list(map(int, new_line[0].split(',')))
        _to = list(map(int, new_line[1].split(',')))
        
        max_axis = max(_from + _to) if max(_from + _to) > max_axis else max_axis
        
        deserialized.append({
            'from': (_from[1], _from[0]),
            'to': (_to[1], _to[0])
        })
    
    return max_axis+1, deserialized

def part1(max_axis, directions):
    board = np.full(
        shape=(max_axis, max_axis), 
        fill_value=0, 
        dtype=int
    )
    
    for direction in directions:
        x1 = direction['from'][0]
        x2 = direction['to'][0]
        
        y1 = direction['from'][1]
        y2 = direction['to'][1]
        # x1 == x2
        if x1 == x2:
            vertical_direction = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)
            for y in vertical_direction:
                board[x1][y] += 1
        # y1 == y2
        elif y1 == y2:
            horizontal_direction = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
            for x in horizontal_direction:
                board[x][y1] += 1
    
    return board, np.count_nonzero(board > 1)

def part2(board, directions):
    for direction in directions:
        x1 = direction['from'][0]
        x2 = direction['to'][0]
        
        y1 = direction['from'][1]
        y2 = direction['to'][1]
        # 1,1 -> 3,3
        if x1 == y1 and x2 == y2:
            left_diagonal = range(x1, y2+1) if x1 <= y2 else range(y2, x1-1, -1)
            for xy in left_diagonal:
                board[xy][xy] += 1
        # 9,7 -> 7,9
        elif x1 == y2 and x2 == y1:
            if x1 <= y1:
                for i in range(0, (y1-x1)+1):
                    board[x1+i][y1-i] += 1
            else:
                for i in range(0, (x1-y1)+1):
                    board[x1-i][y1+i] += 1
        elif not x1 == x2 and not y1 == y2:
            max_xy1 = max(x1, y1)
            max_xy2 = max(x2, y2)
            
            if max_xy1 >= max_xy2:
                for i in range(0, (max_xy1 - max_xy2)+1):
                    board[x1-i][y1-i] += 1
            else:
                for i in range(0, (max_xy2 - max_xy1)+1):
                    board[x1-i][y1+i] += 1
            
    #print(board)
    return np.count_nonzero(board > 1)    
    

if __name__ == '__main__':
    lines = file_to_list('day05.txt', test=False)
    max_axis, lines = get_deserialized_lines(lines)
    
    board, result1 = part1(max_axis, lines)
    print("Day 5, part 1:", result1)
    
    result2 = part2(board, lines)
    print("Day 5, part 2:", result2)    
    