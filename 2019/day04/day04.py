def adjacent(string):
    tmp = dict()
    for item in string:
        if item in tmp.keys():
            tmp[item] += 1
        else:
            tmp[item] = 1
    
    return_items = str()
    for key, value in tmp.items():
        if value >= 2:
            return_items += key*int(key)
    if len(return_items) >= 2:
        return return_items
    return False
        

given_range = (172851, 675869)
cnt = 0
for item in range(given_range[0], given_range[1]):
    if adjacent(str(item)) and sorted(str(item))[0] != '0':
        cnt += 1
print(cnt)
