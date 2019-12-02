opcodes = [1, 2, 99]

with open("day02.txt", "r") as f:
    numbers = [int(x) for x in f.read().split(",")]

print(numbers)

for i in range(len(numbers)):
    if numbers[i] == 1:
        new_numbers = list()
        while numbers[i] != 99:
            new_numbers.append(numbers[i])
            i += 1
        suma = 0
        for j in new_numbers[1:-1]:
            suma += numbers[j]
        numbers[new_numbers[-1]] = suma
    
    
    elif numbers[i] == 2:
        new_numbers = list()
        while numbers[i] != 99:
            new_numbers.append(numbers[i])
            i += 1
        prod = 1
        for j in new_numbers[:-1]:
            prod *= numbers[j]
        numbers[new_numbers[-1]] = prod

print(numbers)