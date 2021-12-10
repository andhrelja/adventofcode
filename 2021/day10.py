from utils import file_to_list
from statistics import median

opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]

syntax_error_score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_score_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part1(lines):
    syntax_error_score = 0
    for line in lines:
        char_ordering = {}
        incorrect_closing_chars = []
        i = 0
        
        for char in line:
            expected_close_char_key = None
            if char_ordering:
                expected_close_char_key = max(char_ordering.keys())
            
            if char in opening_chars:
                char_ordering[i] = char
                i += 1
            elif char in closing_chars and expected_close_char_key:
                open_char = char_ordering[expected_close_char_key]
                expected_close_char = closing_chars[opening_chars.index(open_char)]
                if char != expected_close_char:
                    incorrect_closing_chars.append(char)
                    break
                else:
                    char_ordering.pop(expected_close_char_key)
                    i -= 1
        syntax_error_score += sum((syntax_error_score_table[char] for char in incorrect_closing_chars))
    return syntax_error_score


def part2(lines):
    autocomplete_scores = []
    for line in lines:
        autocomplete_score = 0
        char_ordering = {}
        incorrect_closing_chars = []
        i = 0
        
        for char in line:
            expected_close_char_key = None
            if char_ordering:
                expected_close_char_key = max(char_ordering.keys())
            
            if char in opening_chars:
                char_ordering[i] = char
                i += 1
            elif char in closing_chars and expected_close_char_key:
                open_char = char_ordering[expected_close_char_key]
                expected_close_char = closing_chars[opening_chars.index(open_char)]
                if char != expected_close_char:
                    incorrect_closing_chars.append(char)
                    break
                else:
                    char_ordering.pop(expected_close_char_key)
                    i -= 1

        if not incorrect_closing_chars:
            reversed_char_ordering = list(char_ordering.values())[::-1]
            expected_closing_chars = [closing_chars[opening_chars.index(item)] for item in reversed_char_ordering]
            for char in expected_closing_chars:
                autocomplete_score *= 5
                autocomplete_score += autocomplete_score_table[char]
            autocomplete_scores.append(autocomplete_score)
    return median(sorted(autocomplete_scores))

if __name__ == '__main__':
    lines = file_to_list('day10.txt', test=False)
    
    result1 = part1(lines)
    print("Day 10, part 1:", result1)
    
    result2 = part2(lines)
    print("Day 10, part 2:", result2)
