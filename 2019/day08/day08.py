import numpy as np
import collections


def get_input():
    with open("day08.txt", "r") as f:
        return [int(x) for x in f.read()]

def process(w, h):
    numbers = get_input()
    layers = list()
    k = 0
    while True:
        if k >= len(numbers):
            break
        lst = np.empty(shape=(h, w))
        for i in range(h):
            for j in range(w):
                lst[i][j] = numbers[k]
                k += 1
        layers.append(lst)

    return layers


def get_part1():
    lst = [100, 100]
    for i in range(len(layers)):
        zero_count = np.count_nonzero(layers[i] == 0)
        if zero_count < lst[0]:
            lst[0] = zero_count
            lst[1] = i
    return np.count_nonzero(layers[lst[1]] == 1) * np.count_nonzero(layers[lst[1]] == 2)

def get_part2():
    out = list()

    for layer in layers:
        for i in range(len(layer)):
            if i == 0:
                out.append(min(layer[i]))
            else:
                out.append(min([layer[k] for k in range(i, 0, -1)]))

    return out

layers = process(25, 6)

print("Part 1:", get_part1())
print("Part 2:", get_part2())