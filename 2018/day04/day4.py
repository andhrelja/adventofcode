guards = dict()

with open("day4.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line_split = line.split(" ") 
        if len(line_split) > 4:
            try:
                guards[line_split[3]].append(line_split[0])
                guards[line_split[3]].append(line_split[1])
            except KeyError:
                guards[line_split[3]] = [line_split[0:1]]

    print(guards)