from utils import file_to_list, cleaned

# Incomplete

def get_bag_name(bag_line, contents):
    if isinstance(bag_line, str) and not contents:
        bag_name = bag_line.split(' ')
        return bag_name[0] + '_' + bag_name[1]
    elif isinstance(bag_line, str) and contents:
        bag_name = bag_line.split(' ')
        quantity = bag_name[0]
        if quantity == 'no':
            return None, None
        else:
            return bag_name[1] + '_' + bag_name[2], int(quantity)

    elif isinstance(bag_line, list):
        out = dict()
        for bag in bag_line:
            bag_name, quantity = get_bag_name(bag, contents=True)
            if bag_name and quantity:
                out.update({
                    bag_name: quantity
                })
        return out


def get_structured_input(lines):
    dictionary_list = list()
    for line in lines:
        dictionary = dict()
        split_line = line.split('contain')
        split_line = cleaned(split_line)
        dictionary_key = get_bag_name(split_line[0], contents=False)
        split_bag_contents = split_line[1].split(', ')

        dictionary = {
            dictionary_key: get_bag_name(split_bag_contents, contents=True)
        }
        dictionary_list.append(dictionary)
    return dictionary_list

def part1(dictionary_list, holders=[], bag_name='shiny_gold'):
    for dictionary in dictionary_list:
        for key, item in dictionary.items():
            if bag_name in item.keys() and key not in holders:
                holders.append(key)
                part1(dictionary_list, holders, key)
    return len(holders)

def part2(dictionary_list, counts=[], prev=1, bags_count=0, bag_name='shiny_gold'):
    for dictionary in dictionary_list:
        for key, item in dictionary.items():
            if bag_name == key:
                for key1, value in item.items():
                    bags_count *= value
                    counts.append(bags_count)
                    part2(dictionary_list, counts, value, bags_count, key1)
    return counts


if __name__ == '__main__':
    lines = file_to_list('day07.txt', test=True, sep='.\n')
    dictionary_list = get_structured_input(lines)

    result1 = part1(dictionary_list)
    print("Day 7, part 1:", result1)
    
    result2 = part2(dictionary_list)
    print("Day 7, part 2:", result2)
