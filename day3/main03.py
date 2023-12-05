puzzle_path = 'day3/input03.txt'
example_path = 'day3/example03.txt'

def extract_lines_from_file(file_path):
    # Return a list of lines from a file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines

def find_numbers_in_line(line):
    # Return a list of numbers in a line as strings and their corresponding starting index
    numbers = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            # Number starts at index i and check how long it is
            j = i
            whole_number = ''
            while j < len(line) and line[j].isdigit():
                whole_number += line[j]
                j += 1
            numbers.append([whole_number, i])
            i = j  # Skip over the number we just processed
        else:
            i += 1
    return numbers

def check_neighboring_characters(lines, numbers):
    # lines is a list of 3 consecutive strings
    # numbers is a list of numbers in the middle string
    # Return a list of valid numbers, meaning they are surrounded by a character other than '.'
    truly_valid_numbers = []
    truly_invalid_numbers = []
    previous_line = lines[0]
    current_line = lines[1]
    next_line = lines[2]
    [valid_numbers, invalid_numbers] = check_same_line(current_line, numbers)
    if valid_numbers:
        truly_valid_numbers.extend(valid_numbers)
    [valid_numbers, invalid_numbers] = check_other_line(previous_line, invalid_numbers)
    if valid_numbers:
        truly_valid_numbers.extend(valid_numbers)
    [valid_numbers, invalid_numbers] = check_other_line(next_line, invalid_numbers)
    if valid_numbers:
        truly_valid_numbers.extend(valid_numbers)
    if invalid_numbers:
        truly_invalid_numbers.extend(invalid_numbers)

    return [truly_valid_numbers, truly_invalid_numbers]

def check_same_line(line, numbers):
    # line is a string
    # numbers is a list of numbers in the line
    # Return a list of valid numbers, meaning they are surrounded by a character other than '.'
    valid_numbers = []
    invalid_numbers = []
    for number in numbers:
        # number contains the number as a string and its starting index
        # Check the character before and after the number
        # If they are not '.', then the number is valid

        # note: this does not work for the first and last number in the line
        # make a special case for those
        
        if number[1] == 0 or number[1] == len(line)-len(number[0]):
            # No character before or after the number
            # Check if the number is surrounded by a character
            if number[1] == 0:
                if line[number[1]+len(number[0])] != '.':
                    # Number is valid because it is not surrounded by '.' (or a number)
                    # meaning that is must be surrounded by a character
                    valid_numbers.append(number)
                else:
                    invalid_numbers.append(number)
            else:
                if line[number[1]-1] != '.':
                    # Number is valid because it is not surrounded by '.' (or a number)
                    # meaning that is must be surrounded by a character
                    valid_numbers.append(number)
                else:
                    invalid_numbers.append(number)
            continue
        elif line[number[1]-1] != '.' or line[number[1]+len(number[0])] != '.':
            # Number is valid because it is not surrounded by '.' (or a number)
            # meaning that is must be surrounded by a character
            valid_numbers.append(number)
        else:
            invalid_numbers.append(number)
        continue
    return [valid_numbers, invalid_numbers]

def check_other_line(other_line, numbers):
    # Return a list of valid numbers, meaning they are surrounded by a character other than '.'
    valid_numbers = []
    invalid_numbers = []
    for number in numbers:
        # number contains the number as a string and its starting index
        # Check the line above for characters
        # If they are not '.' or a digit, then the number is valid
        # is_valid = False
        if number[1] == 0:
            f = 0
        else:
            f = 1

        if number[1] == len(other_line)-1:
            l = 0
        else:
            l = 1
        start = number[1]-f
        end = start+len(number[0])+1+l
        if contains_only_dots_and_digits(other_line[start:end]):
            invalid_numbers.append(number)
        else:
            valid_numbers.append(number)

    return [valid_numbers, invalid_numbers]

def contains_only_dots_and_digits(s):
    return all(c.isdigit() or c == '.' for c in s)  

def main03a(filepath):
    lines = extract_lines_from_file(filepath)
    # lines = lines[22:25]
    # print(f'Lines: {lines}\n')
    valid_numbers = []
    invalid_numbers = []
    # add empty line in the beggining and end of the list and then loop through 3 consecutive lines
    empty_line = '.'*len(lines[0])
    lines.insert(0, empty_line)
    lines.append(empty_line)
   # loop through each line
    for i in range(1, len(lines)-1):
        # Find numbers in the line
        numbers = find_numbers_in_line(lines[i])
        # Check the neighboring characters
        [valid_numbers_in_line, invalid_numbers_in_line] = check_neighboring_characters(lines[i-1:i+2], numbers)
        if valid_numbers_in_line:
            valid_numbers.extend(valid_numbers_in_line)
        if invalid_numbers_in_line:
            invalid_numbers.extend(invalid_numbers_in_line)
    # print(f'Lines: {lines}\n')
    # print(f'Valid numbers: {valid_numbers}\n')
    # print(f'Invalid numbers: {invalid_numbers}')
    return sum([int(number[0]) for number in valid_numbers])

def main03a_error(filepath):
    try:
        lines = extract_lines_from_file(filepath)
        valid_numbers = []
        invalid_numbers = []
        # add empty line in the beginning and end of the list and then loop through 3 consecutive lines
        empty_line = '.' * len(lines[0])
        lines.insert(0, empty_line)
        lines.append(empty_line)
        # loop through each line
        for i in range(1, len(lines) - 1):
            # Find numbers in the line
            numbers = find_numbers_in_line(lines[i])
            # Check the neighboring characters
            [valid_numbers_in_line, invalid_numbers_in_line] = check_neighboring_characters(lines[i - 1:i + 2], numbers)
            if valid_numbers_in_line:
                valid_numbers.extend(valid_numbers_in_line)
            if invalid_numbers_in_line:
                invalid_numbers.extend(invalid_numbers_in_line)
        return sum([int(number[0]) for number in valid_numbers])
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print(f"Error on line {i} with content: {lines[i]}")
        # Optionally, print out more details about the variables or state of the program
        # to help diagnose the problem.

print(main03a(puzzle_path))
# main03a_error(puzzle_path)