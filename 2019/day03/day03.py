import numpy


def get_lines():
    with open("day03.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines[0].split(","), lines[1].split(",")


def draw_line(array, line):
    i,j = array.shape[0] // 2, array.shape[1] // 2
    array[i][j] = 'o'

    for item in line:
        curr_i, curr_j = i, j
        if item.startswith("U"):
            while i > (curr_i - int(item[1:])):
                if array[i-1][j] == ".":
                    array[i-1][j] = "|"
                else:
                    array[i-1][j] = "X"
                i -= 1

        elif item.startswith("D"):
            while i < (curr_i + int(item[1:])):
                if array[i+1][j] == ".":
                    array[i+1][j] = "|"
                else:
                    array[i+1][j] = "X"
                i += 1
                
        elif item.startswith("L"):
            while j > (curr_j - int(item[1:])):
                if array[i][j-1] == ".":
                    array[i][j-1] = "-"
                else:
                    array[i][j-1] = "X"
                j -= 1
                        
        elif item.startswith("R"):
            while j < (curr_j + int(item[1:])):
                if array[i][j+1] == ".":
                    array[i][j+1] = "-"
                else:
                    array[i][j+1] = "X"
                j += 1
              

    return array


def get_part1():
    shape = (20, 20)
    array = numpy.empty(shape, dtype=object)
    array.tostring()
    array[:] = "."

    line1, line2 = get_lines()
    array = draw_line(array, line1)
    array = draw_line(array, line2)
    numpy.savetxt("output.txt", X=array, fmt="%s")

    min_sum = list()
    for i in range(shape[0]):
        for j in range(shape[0]):
            if array[i][j] == "X":
                min_sum.append((i, j))
    
    o = shape[0] // 2
    for item in min_sum:
        print(abs(o - item[0]) + abs(o - item[1]))
            


get_part1()
