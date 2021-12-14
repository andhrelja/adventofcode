from utils import file_to_list
import numpy as np

def get_deserialized_lines(lines):
    coordinates, folds = lines
    coordinates = coordinates.split("\n")
    coordinates = [list(map(int, coordinate.split(","))) for coordinate in coordinates]
    folds = folds.replace('fold along ', '')
    folds = folds.split("\n")
    new_folds = []
    fold_dict = {}
    for fold in folds:
        ax, i = fold.split("=")
        if ax in fold_dict.keys():
            new_folds.append(fold_dict)
            fold_dict = {}
        fold_dict.update({ax: int(i)})
    new_folds.append(fold_dict)
    return coordinates, new_folds

def print_lines(arr):
    print_str = ""
    for item in arr:
        print_str += "".join(item) + "\n"
    
    print(print_str)

def get_folded_array(arr, value, direction):   
    if direction == 'y':
        arr1 = arr[:value, :]
        arr2 = arr[value:, :]
        arr2 = arr2[::-1,:]
    else:
        arr1 = arr[:, :value]
        arr2 = arr[:, value:]
        arr2 = arr2[:,::-1]
    
    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            if arr2[i, j] == '#':
                arr1[i, j] = arr2[i, j]
    return arr1

def part1(lines, folds, max_folds=1):
    lines = [(x, y) for y, x in lines]
    max_x = max(coord[0] for coord in lines)
    max_y = max(coord[1] for coord in lines)
    arr = np.full(shape=(max_x+1, max_y+1), fill_value=' ')
    
    for coord in lines:
        arr[coord] = '#'
        
    for fold in folds[:max_folds]:
        for key, value in list(fold.items())[:max_folds]:
            arr = get_folded_array(arr, value, key)
    return np.count_nonzero(arr == '#')

def part2(lines, folds):
    lines = [(x, y) for y, x in lines]
    max_x = max(coord[0] for coord in lines)
    max_y = max(coord[1] for coord in lines)
    arr = np.full(shape=(max_x+1, max_y+1), fill_value=' ')
    
    for coord in lines:
        arr[coord] = '#'
        
    for fold in folds:
        for key, value in fold.items():
            arr = get_folded_array(arr, value, key)
    print_lines(arr)
    return np.count_nonzero(arr == '#')

if __name__ == '__main__':
    lines = file_to_list('day13.txt', test=False, sep='\n\n')
    coordinates, folds = get_deserialized_lines(lines)
    
    result1 = part1(coordinates, folds, max_folds=1)
    print("Day 13, part 1:", result1)
    
    result2 = part2(coordinates, folds)
    print("Day 13, part 2:", result2)
    
    # Needs improvement
    #  # #### #### #### # ## # ## #  # # ##
    #  # #### # ## #### #### #### #  # ####
    #  # ###  ####   ## ###  #### #  #  ###
    #  # # #  #### ###  # #  #### #  # ##
    ## # #    #### ## # # ## #### #### ####
     ##  #    # ## ###  # ## #  # #### # ##
    