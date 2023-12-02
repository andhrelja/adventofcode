from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

stripped = lambda x: [i.strip() for i in x]

def file_to_list(filename, test=False, sep=None, cast=None, strip=True):
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
            lines = stripped(lines)
        
        if cast:
            return list(map(cast, lines))
        else:
            return lines
