from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

diagonal_neighbours = lambda i, j, lines: [
    lines[i-1][j-1], # nw
    lines[i-1][j+1], # ne
    lines[i+1][j-1], # sw
    lines[i+1][j+1], # se
]

adjacent_neighbours = lambda i, j, lines: [
    lines[i][j-1], # n
    lines[i][j+1], # s
    lines[i-1][j], # w
    lines[i+1][j], # e
]

all_neighbours = lambda i, j, lines: [
    *diagonal_neighbours(i, j, lines),
    *adjacent_neighbours(i, j, lines)
]

def file_to_list(filename, test=False, sep=None, strip=True, _map=None):
    if test:
        filepath = BASE_DIR / 'test_inputs' / filename
    else:
        filepath = BASE_DIR / 'inputs' / filename
    
    with open(filepath, 'r') as f:
        if sep is None:
            lines = f.readlines()
        else:
            lines = f.read()
            lines = lines.split(sep)
        
        if strip:
            lines = map(str.strip, lines)
        
        if _map:
            return map(_map, lines)
        else:
            return lines
