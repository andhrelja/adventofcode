from utils import file_to_list


def serialize_input(lines, _map=int):
    left, right = [], []
    for line in lines:
        l, r = map(_map, line.split())
        left.append(l)
        right.append(r)
    return (left, right)


def part1(lines):
    dists = []
    left, right = serialize_input(lines)
    for l, r in zip(sorted(left), sorted(right)):
        dists.append(abs(l - r))
    return sum(dists)


def part2(lines):
    sims = []
    left, right = map("".join, serialize_input(lines, _map=str))
    for l in left:
        sim = right.count(l)
        sims.append(sim * int(l))
    return sum(sims)


if __name__ == "__main__":
    lines = list(file_to_list("day01.txt", test=False))

    result1 = part1(lines)
    print("Day 1, part 1:", result1)

    result2 = part2(lines)
    # 12279932 wrong
    print("Day 1, part 2:", result2)
