from utils import file_to_list

def get_deserialized_lines(lines):
    deserialized = {}
    for line in lines:
        key, value = line.split("-")
        if key not in deserialized.keys():
            deserialized[key] = []
        if value not in deserialized.keys():
            deserialized[value] = []
        
        if value != 'start':
            deserialized[key].append(value)
        if key != 'start':
            deserialized[value].append(key)
    return deserialized

def get_valid_path(graph, start_key, valid_path, visited):
    if start_key not in visited.keys():
        visited[start_key] = []
    if start_key == 'end':
        return valid_path
    
    for key in graph[start_key]:
        if key.lower() == key and any(val.upper() == val for val in graph[key]):
            if key not in visited[start_key]:
                valid_path.append(key)
                visited[start_key].append(key)
                valid_path = get_valid_path(graph, key, valid_path, visited)
        elif key.upper() == key:
            if key not in visited[start_key]:
                valid_path.append(key)
                visited[start_key].append(key)
                valid_path = get_valid_path(graph, key, valid_path, visited)
    return valid_path

def part1(graph):
    valid_paths = []
    for value in graph['start']:
        valid_path = get_valid_path(graph, value, ['start', value], {})
        valid_paths.append(valid_path)

    return valid_paths

def part2(lines):
    return


if __name__ == '__main__':
    lines = file_to_list("day12.txt", test=True)
    lines = get_deserialized_lines(lines)

    result1 = part1(lines)
    print("Day 12, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 12, part 2:", result2)
