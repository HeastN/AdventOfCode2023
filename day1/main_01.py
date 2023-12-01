input_file = '/home/robin/AdventOfCode/AdventOfCode2023/day1/input.txt'
example2 = '/home/robin/AdventOfCode/AdventOfCode2023/day1/example2.txt'

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
rev_words = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
def create_word_dict(words):
    # Create a dictionary of words and their corresponding numbers
    # e.g. {'one': 1, 'two': 2, ...} up to 9
    word_dict = {}
    for i in range(10):
        word_dict[words[i]] = i
    return word_dict

word_dict = create_word_dict(words)
rev_word_dict = create_word_dict(rev_words)

def extract_lines_from_file(file_path):
    # Return a list of lines from a file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines
    
def extract_int_pairs_from_line(line):
    # Return a list of the first and last number in a line
    int_pair = [0,0]
    first_number = 0
    last_number = 0
    first_number_found = False
    last_number_found = False
    reversed_line = line[::-1]

    for i in range(len(line)):
        if line[i].isdigit() and first_number_found == False:
            first_number = int(line[i])
            int_pair[0] = first_number
            first_number_found = True
        if reversed_line[i].isdigit() and last_number_found == False:
            last_number = int(reversed_line[i])
            int_pair[1] = last_number
            last_number_found = True
        if first_number_found and last_number_found:
            break
    return int_pair

def get_number(int_pairs):
    # Return the number that the two digits form
    # e.g. (1, 2) -> 12
    return int(str(int_pairs[0]) + str(int_pairs[1]))

def extract_pair_from_line(line):
    # Return a list of the first and last number in a line
    number_pair = [0,0]
    first_word_candidate = ''
    last_word_candidate = ''
    first_number = 0
    last_number = 0
    first_number_found = False
    last_number_found = False
    reversed_line = line[::-1]

    for i in range(len(line)):
        if not first_number_found:
            if line[i].isdigit():
                first_number = int(line[i])
                number_pair[0] = first_number
                first_number_found = True
            elif line[i].isalpha():
                first_word_candidate += line[i].lower()
                if not any(key.startswith(first_word_candidate) for key in word_dict):
                    # Reset the candidate if it doesn't match any keys
                    first_word_candidate = line[i].lower()
                if first_word_candidate in word_dict:
                    # if the key is in the dictionary, then we have a match
                    first_number = word_dict[first_word_candidate]
                    number_pair[0] = first_number
                    first_number_found = True
        if not last_number_found:
            if reversed_line[i].isdigit():
                last_number = int(reversed_line[i])
                number_pair[1] = last_number
                last_number_found = True
            elif reversed_line[i].isalpha():
                last_word_candidate += reversed_line[i].lower()
                if not any(key.startswith(last_word_candidate) for key in rev_word_dict):
                    # Reset the candidate if it doesn't match any keys
                    last_word_candidate = reversed_line[i].lower()
                if last_word_candidate in rev_word_dict:
                    # if the key is in the dictionary, then we have a match
                    last_number = rev_word_dict[last_word_candidate]
                    number_pair[1] = last_number
                    last_number_found = True
        elif first_number_found and last_number_found:
            break
    return number_pair

def main_01a(input_file):
    lines = extract_lines_from_file(input_file)
    total_sum = 0
    for line in lines:
        int_pair = extract_int_pairs_from_line(line)
        number = get_number(int_pair)
        total_sum += number
    return total_sum

def main_01b(input_file):
    lines = extract_lines_from_file(input_file)
    lines = lines[40:50]
    total_sum = 0
    for line in lines:
        int_pair = extract_pair_from_line(line)
        number = get_number(int_pair)
        print(f'line: {line}, int_pair: {int_pair} -> {number}\n')
        total_sum += number
    return total_sum

print(main_01a(input_file))
print(main_01b(input_file))
