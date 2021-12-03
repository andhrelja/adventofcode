from utils import file_to_list


def get_deserialized_lines(lines):
    deserialized = []
    for line in lines:
        new_line = list(line)
        deserialized.append(new_line)
    return deserialized

def get_serialized_line(line):
    return "".join(map(str, line))

def get_gamma_epsilon(deserialized_gamma, deserialized_epsilon):
    gamma_binary_string = get_serialized_line(deserialized_gamma)
    epsilon_binary_string = get_serialized_line(deserialized_epsilon)
    
    gamma = int(gamma_binary_string, base=2)
    epsilon = int(epsilon_binary_string, base=2)
    return gamma, epsilon

def part1(lines, return_result=True):
    len_x = len(lines[0])
    len_y = len(lines)
    
    most_common_bits = {i: -1 for i in range(len_x)}
    least_common_bits = {i: -1 for i in range(len_x)}
    
    for i in range(len_x):
        count_0 = 0
        count_1 = 0
        
        for j in range(len_y):
            if lines[j][i] == '0':
                count_0 += 1
            elif lines[j][i] == '1':
                count_1 += 1
        
        if count_0 > count_1:
            most_common_bits[i] = 0
            least_common_bits[i] = 1
        else:
            most_common_bits[i] = 1
            least_common_bits[i] = 0
            
    assert -1 not in most_common_bits.values()
    assert -1 not in least_common_bits.values()
    
    gamma, epsilon = get_gamma_epsilon(most_common_bits.values(), least_common_bits.values())
    
    if return_result:
        return gamma * epsilon
    else:
        return most_common_bits, least_common_bits

def part2(ogr, co2sr, common_index=0):
    if len(ogr) == 1 and len(co2sr) == 1:
        gamma, epsilon = get_gamma_epsilon(ogr[0], co2sr[0])
        return gamma * epsilon
    
    most_common_bits, _ = part1(ogr, return_result=False)
    _, least_common_bits = part1(co2sr, return_result=False)
    
    if len(ogr) > 1:
        ogr = [item for item in ogr if item[common_index] == str(most_common_bits[common_index])]
    if len(co2sr) > 1:
        co2sr = [item for item in co2sr if item[common_index] == str(least_common_bits[common_index])]
    return part2(ogr, co2sr, common_index+1)
    
            
if __name__ == '__main__':
    lines = file_to_list('day03.txt', test=False)
    lines = get_deserialized_lines(lines)
    
    result1 = part1(lines, return_result=True)
    print("Day 3, part 1:", result1)
    
    result2 = part2(lines, lines)
    print("Day 3, part 2:", result2)    
