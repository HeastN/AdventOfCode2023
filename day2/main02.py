filepath = 'day2/input02.txt'

def extract_lines_from_file(file_path):
    # Return a list of lines from a file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines

def check_game(red_max, green_max, blue_max, line):
    # Check if a game is valid
    # Return the game id and if it is valid or not
    # A game is valid if it has less than the max amount of red, green or blue
    [game_id_string, game] = line.split(':')
    game_id = int(game_id_string.rstrip().split(' ')[-1])
    sets = game.split(';')
    for set in sets:
        # Go through each set and check if any color has more than the amount
        # of red, green or blue
        amount_of_red = calculate_amount_of_color('red', set)
        amount_of_green = calculate_amount_of_color('green', set)
        amount_of_blue = calculate_amount_of_color('blue', set)
        if amount_of_red > int(red_max) or amount_of_green > int(green_max) or amount_of_blue > int(blue_max):
            return [game_id, False]       
    return [game_id, True]

def check_game2(line):
    [game_id_string, game] = line.split(':')
    game_id = int(game_id_string.rstrip().split(' ')[-1])
    sets = game.split(';')
    max_red_found = 1
    max_green_found = 1
    max_blue_found = 1
    for set in sets:
        # Go through each set and check if any color has more than the amount
        # of red, green or blue
        amount_of_red = calculate_amount_of_color('red', set)
        amount_of_green = calculate_amount_of_color('green', set)
        amount_of_blue = calculate_amount_of_color('blue', set)
        if amount_of_red > max_red_found:
            max_red_found = amount_of_red
        if amount_of_green > max_green_found:
            max_green_found = amount_of_green
        if amount_of_blue > max_blue_found:
            max_blue_found = amount_of_blue
    return max_red_found*max_green_found*max_blue_found

def calculate_amount_of_color(color, set):
    # Return the amount of the color in the set
    
    # Split the set into a list of colors
    colors = set.split(',')
    for color_string in colors:
        if color in color_string:
            # If the color is in the color_string, return the amount of the color
            return int(color_string.lstrip().split(' ')[0])
    # If the color is not in the set, return 0
    return 0


def main02a(amount_red, amount_green, amount_blue):
    lines = extract_lines_from_file(filepath)
    # lines = lines[0:3]
    id_sum = 0
    for line in lines:
        # Go through each line and check if any game id 
        # has more than the amount of red, green or blue
        [game_id, valid] = check_game(amount_red, amount_green, amount_blue, line)
        if valid:
            id_sum += game_id
    print(f'sum of all ids: {id_sum}')
    return id_sum

def main02b():
    lines = extract_lines_from_file(filepath)
    # lines = lines[0:3]
    power_sum = 0
    for line in lines:
        # Go through each line and check if any game id 
        # has more than the amount of red, green or blue
        power = check_game2(line)
        power_sum += power
    print(f'sum of all powers: {power_sum}')
    return power_sum

main02a(12, 13, 14)
main02b()


