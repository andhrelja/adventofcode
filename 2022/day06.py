from utils import file_to_list


def solve(lines, packet_size=4):
    for line in lines:
        for i, char in enumerate(line):
            charset = line[i:i+packet_size]
            if len(charset) == len(set(charset)):
                yield i+packet_size
                break

if __name__ == '__main__':
    lines = file_to_list('day06.txt', test=False, sep='\n')
    
    result1 = list(solve(lines, packet_size=4))
    print("Day 6, part 1:", result1)
    
    result2 = list(solve(lines, packet_size=14))
    print("Day 6, part 2:", result2)
