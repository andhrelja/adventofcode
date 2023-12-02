from utils import file_to_list
import numpy as np

LOAD_CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def serialize_input(lines):
    for line in lines:
        game_name, cube_sets = line.split(':')
        cube_sets = map(str.strip, cube_sets.split(';'))
        cube_sets = [
            [
                {
                    'amount': item.strip().split(' ')[0],
                    'color': item.strip().split(' ')[1],
                } for item in map(str.strip, sets.split(','))]
            for sets in cube_sets
        ]

        total_sets, min_sets = {}, {}
        for col in LOAD_CONFIG:
            total_sets[col] = total_sets.get(col, [])
            for sets in cube_sets:
                total_sets[col].extend(list(map(
                    lambda x: int(x['amount']), 
                    filter(lambda x: x['color'] == col, 
                        sets))))
            min_sets[col] = max(total_sets[col])

        yield dict(
            game_id=int(game_name.replace('Game ', '')),
            cube_sets=cube_sets,
            total_sets=total_sets,
            min_sets=min_sets
        )


def part1(lines):
    contents = serialize_input(lines)
    possible_ids, impossible_ids = [], []
    for game in contents:
        if any((amount > LOAD_CONFIG[color] 
                for color, amounts in game['total_sets'].items()
                for amount in amounts)):
            impossible_ids.append(game['game_id'])
        else:    
            possible_ids.append(game['game_id'])
    return sum(possible_ids)


def part2(lines):
    contents = serialize_input(lines)
    cube_pows = []
    for game in contents:
        cube_pows.append(np.prod(list(game['min_sets'].values())))
    return sum(cube_pows)



if __name__ == '__main__':
    lines = file_to_list('day02.txt', test=False)
        
    result1 = part1(lines)
    print("Day 2, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 2, part 2:", result2)
