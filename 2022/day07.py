from utils import file_to_list


class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self._size = size
        self.children = []
    
    @property
    def size(self):
        return sum((child.size for child in self.children))
    
    def add_child(self, child):
        self.children.append(child)

    def get_height(self):
        height = 0
        parent = self.parent
        while parent:
            parent = parent.parent
            height += 1
        return height

    def __repr__(self):
        return self.name


class Directory(Node):
    def __str__(self):
        children_str = '\n'.join(('{}{}'.format('  '*child.get_height(), child) for child in sorted(self.children, key=lambda x: x.name)))
        return '- {} (dir)\n{}'.format(self.name, children_str)


class File(Node):
    @property
    def size(self):
        return self._size
    
    def __str__(self):
        return '- {} (size={})'.format(self.name, self._size)


def directory_sizes(root, size_filter, sizes=[]):
    for child in filter(lambda x: isinstance(x, Directory), root.children):
        if size_filter(child.size):
            sizes.append(child.size)
        directory_sizes(child, size_filter, sizes)
    return sizes


def get_input(lines):
    ls = False
    root = Directory('/')
    node = root
    for line in lines:
        if line.startswith('$ ls'):
            ls = True
            continue
        
        if line.startswith('$ cd ..'):
            ls = False
            node = node.parent
            
        if line.startswith('$ cd') and line != '$ cd ..':
            ls = False
            dir_name = line.replace('$ cd', '').strip()
            new_node = Directory(dir_name, parent=node)           
            node.add_child(new_node)
            node = new_node
        
        if ls and not line.startswith('dir '):
            file_size, file_name = line.split()
            file = File(name=file_name, size=int(file_size), parent=node)
            node.add_child(file)
    
    return root


if __name__ == '__main__':
    lines = file_to_list('day07.txt', test=False)[1:]
    root = get_input(lines)
    
    part1 = 100_000
    print("Day 7, part 1:", sum(directory_sizes(root, lambda x: x < part1)))
    
    part2 = 30_000_000 - (70_000_000 - root.size)
    print("Day 7, part 2:", min(directory_sizes(root, lambda x: x > part2)))
