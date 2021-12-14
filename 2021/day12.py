from utils import file_to_list

NODES = []

class Node:
    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbours
        self.path = []

    @staticmethod
    def get(value):
        for node in NODES:
            if node.value == value:
                return node
        return None

    def create_paths(self, path=[]):
        #self.path = path
        if self.value is None:
            path.append(None)
            return path
        
        if self.value.islower() and self not in path and any(nn.isupper() for nn in self.neighbours):
            path.append(self)
        elif self.value.isupper():
            path.append(self)
        else:
            return None
        
        self.path = path
        paths = []
        for neighbour in self.neighbours:
            neighbour = Node.get(neighbour)
            _path = neighbour.create_paths(path)
            if _path: 
                paths.append(_path)
                path = self.path
        return paths

    def __repr__(self):
        return self.value


def populate_nodes(graph):
    is_end_node = lambda x: None if x == 'end' else x
    for root, neighbours in graph.items():
        neighbours = list(map(is_end_node, neighbours))
        root = None if root == 'end' else root
        node = Node(root, neighbours)
        NODES.append(node)

def part1(lines):
    populate_nodes(lines)
    paths = []
    for root in lines['start']:
        node = Node.get(root)
        path = node.create_paths()
        if path:
            paths += path
        #paths.append(path)
    print(paths)

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
    #deserialized.pop('end')
    return deserialized

def part2(lines):
    return


if __name__ == '__main__':
    lines = file_to_list("day12.txt", test=True)
    lines = get_deserialized_lines(lines)

    result1 = part1(lines)
    print("Day 12, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 12, part 2:", result2)
