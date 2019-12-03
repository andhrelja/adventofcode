import numpy


def get_lines():
    with open("day03.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines[0].split(","), lines[1].split(",")


def draw_line(array, line):
    curr_i, curr_j = array.shape[0] // 2, array.shape[1] // 2
    i,j = array.shape[0] // 2, array.shape[1] // 2
    k = 0
    for item in line:
        if item.startswith("R"):
            while j < (curr_j + int(item[1:])):
                if k == 0:
                    array[i][j] = 3
                    k = 1
                else:
                    if array[i][j] == 0:
                        array[i][j] = 1
                    elif array[i][j] == 1:
                        array[i][j] = 2
                j += 1
                
        elif item.startswith("L"):
            while j > (curr_j - int(item[1:])):
                if k == 0:
                    array[i][j] = 3
                    k = 1
                else:
                    if array[i][j] == 0:
                        array[i][j] = 1
                    elif array[i][j] == 1:
                        array[i][j] = 2
                j -= 1
        elif item.startswith("U"):
            while i < (curr_i + int(item[1:])):
                if k == 0:
                    array[i][j] = 3
                    k = 1
                else:
                    if array[i][j] == 0:
                        array[i][j] = 1
                    elif array[i][j] == 1:
                        array[i][j] = 2
                i += 1
        elif item.startswith("D"):
            while i > (curr_i - int(item[1:])):
                if k == 0:
                    array[i][j] = 3
                    k = 1
                else:
                    if array[i][j] == 0:
                        array[i][j] = 1
                    elif array[i][j] == 1:
                        array[i][j] = 2
                i -= 1
    return array


def get_part1():
    array = numpy.zeros((20, 20), dtype=int)
    line1, line2 = get_lines()
    array = draw_line(array, line1)
    array = draw_line(array, line2)
    numpy.savetxt("output.txt", X=array.astype(int), fmt='%i')


get_part1()
