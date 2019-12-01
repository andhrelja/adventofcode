import numpy
import re

count = 0
matrix = numpy.zeros(shape=(1500, 1500))
visited = list()

with open("day3.txt", "r") as f:
    lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    for line in lines:
        id, left, top, width, height = map(int, re.findall(r'\d+', line))

        for i in range(top, top + height):
            for j in range(left, left + width):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = 2
                    count += 1
        
with open("3.txt", "w") as fw:
    write_string = ""
    for i in range(0, 1500):
        for j in range(0, 1500):
            if j == 1499:
                write_string += '\n'
            if matrix[i][j] == 0:
                write_string += "."
            elif matrix[i][j] == 1:
                write_string += "#"
            elif matrix[i][j] == 2:
                write_string += "X"
    
    fw.write(write_string)
        

print(count)