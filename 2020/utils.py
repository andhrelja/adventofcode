from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

cleaned = lambda x: [i.strip() for i in x]

def file_to_list(filename, test=False, sep=None, cast=None):
    if test:
        filepath = BASE_DIR / 'test_inputs' / filename
    else:
        filepath = BASE_DIR / 'inputs' / filename
    
    with open(filepath, 'r') as f:
        if not sep:
            lines = f.readlines()
        else:
            lines = f.read()
            lines = lines.split(sep)
        lines = cleaned(lines)
        
        if cast:
            return list(map(cast, lines))
        else:
            return lines
