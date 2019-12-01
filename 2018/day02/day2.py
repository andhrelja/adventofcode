
letters = dict()

with open("day2.txt", 'r') as f:
    lines = f.readlines()
    
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    for i in range(0, len(lines)):
        letters[lines[i]] = list()
        for j in range(0, len(lines)):
            if i is not j:
                counter = 0
                for k in range(0, len(lines[j])):
                    if lines[i][k] != lines[j][k]:
                        counter += 1
                letters[lines[i]].append(counter)

    for l in letters:
        if 1 in letters[l]:
            print(l)
