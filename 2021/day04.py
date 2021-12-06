from utils import file_to_list
import copy

def get_deserialized_lines(lines):
    numbers_to_draw = lines.pop(0).split(",")
    numbers_to_draw = list(map(int, numbers_to_draw))
    lines.pop(0)
    deserialized_matrices = []
    deserialized_matrix = []
    for line in lines:
        line = line.replace("  ", " ")
        if line == '':
            deserialized_matrices.append(deserialized_matrix)
            deserialized_matrix = []
        else:
            split_line = line.split(" ")
            split_line = list(map(int, split_line))
            deserialized_matrix.append(split_line)
    deserialized_matrices.append(deserialized_matrix)
    return numbers_to_draw, deserialized_matrices

def get_transposed_matrix(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0])):
        transposed_row = []
        for i in range(len(matrix)):
            transposed_row.append(matrix[i][j])
        transposed_matrix.append(transposed_row)
    return transposed_matrix

def is_winner(drawn_nums, matrix):
    drawn_nums = set(drawn_nums)
    transposed_matrix = get_transposed_matrix(matrix)
    for mat_row, t_mat_row in zip(matrix, transposed_matrix):
        mat_row = set(mat_row)
        t_mat_row = set(t_mat_row)
        if mat_row.issubset(drawn_nums):
            return True
        if t_mat_row.issubset(drawn_nums):
            return True
    return False

def get_solution(drawn_nums, matrix):
    unmarked_sum = 0
    for mat_row in matrix:
        for row_num in mat_row:
            if row_num not in drawn_nums:
                unmarked_sum += row_num
    return unmarked_sum * drawn_nums[-1]

def print_winner(drawn_nums, matrix):
    print(drawn_nums, "\n")
    out = []
    for mat_row in matrix:
        new_row = []
        for row_num in mat_row:
            if row_num in drawn_nums:
                new_row.append(str(row_num)+'*')
            else:
                new_row.append(str(row_num))
        out.append("\t".join(new_row))
    print("\n".join(out))

def part1(nums, matrices):
    min_subset_items = 5
    nums_subset = nums[:min_subset_items]
    
    winner = False
    while winner is False:
        nums_subset.append(nums[min_subset_items])
        for i, matrix in enumerate(matrices):
            winner = is_winner(nums_subset, matrix)
            if winner:
                break
        min_subset_items += 1
    return get_solution(nums_subset, matrix)

def part2(nums, matrices):
    min_subset_items = 5
    nums_subset = nums[:min_subset_items]
    
    winners = []
    winner = False
    
    while min_subset_items < len(nums):
        nums_subset.append(nums[min_subset_items])
        for i, matrix in enumerate(matrices):
            winner = is_winner(nums_subset, matrix)
            if winner and i not in (item[0] for item in winners):
                winners.append((i, matrix, copy.deepcopy(nums_subset)))
                winner = False
        min_subset_items += 1
    return get_solution(winners[-1][2], winners[-1][1])

if __name__ == '__main__':
    lines = file_to_list('day04.txt', test=False)
    nums, matrices = get_deserialized_lines(lines)
    
    result1 = part1(nums, matrices)
    print("Day 4, part 1:", result1)
    
    result2 = part2(nums, matrices)
    print("Day 4, part 2:", result2)
