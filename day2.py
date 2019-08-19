def process(filename="day2.txt"):
    letters = dict()

    with open(filename, 'r') as f:
        lines = f.readlines()
        
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()

        for i in range(0, len(lines)):
            letters[lines[i]] = list()
            for j in range(0, len(lines)):
                if i is not j:
                    counter = 0
                    for k in range(0, len(lines[j])):
                        if lines[i][k] == lines[j][k]:
                            counter += 1
                    letters[lines[i]].append(counter)
        print(letters)

        max_key = dict()
        for key in letters:
            max_key[key] = max(letters[key])
        
        print(max([max_key[key] for key in max_key]))

        print(max_key)


process()