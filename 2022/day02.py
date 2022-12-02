from utils import file_to_list

outcome_points = {
    'victory': 6,
    'draw': 3,
    'loss': 0
}

definitions = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

plays = {
    'rock': {
        'score': 1,
        'rock': 'draw',
        'paper': 'loss',
        'scissors': 'victory'
    },
    'paper': {
        'score': 2,
        'rock': 'victory',
        'paper': 'draw',
        'scissors': 'loss'        
    },
    'scissors': {
        'score': 3,
        'rock': 'loss',
        'paper': 'victory',
        'scissors': 'draw'      
    }
}


def part1(lines):
    definitions['X'] = 'rock'
    definitions['Y'] = 'paper'
    definitions['Z'] = 'scissors'
    
    total_points = 0
    
    for line in lines:
        player_1 = definitions[line[0]] # rock
        player_2 = definitions[line[1]] # paper
        player_2_play = plays[player_2]
        total_points += outcome_points[player_2_play[player_1]] + player_2_play['score']
    return total_points


def part2(lines):
    definitions['X'] = ('loss', 'victory')
    definitions['Y'] = ('draw', 'draw')
    definitions['Z'] = ('victory', 'loss')
    
    total_points = 0
    for line in lines:
        player_1 = definitions[line[0]]
        
        player_2_outcome_inv = definitions[line[1]][1]
        player_2_outcome = definitions[line[1]][0]
        player_2 = [k for k in plays.keys() if plays[player_1][k] == player_2_outcome_inv][0]

        player_2_play = plays[player_2]
        total_points += outcome_points[player_2_outcome] + player_2_play['score']
    return total_points


if __name__ == '__main__':
    lines = file_to_list('day02.txt', test=False)
    lines = [line.split() for line in lines]
        
    result1 = part1(lines)
    print("Day 2, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 2, part 2:", result2)
