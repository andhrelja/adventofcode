from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

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
