example_path = 'day4/example04.txt'
puzzle_path = 'day4/input04.txt'

def extract_lines_from_file(file_path):
    # Return a list of lines from a file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines
    
def divide_string(line):
    # Divide a string into 3 parts: game id, winning numbers, and ticket numbers
    parts = line.split('|')

    game_id_and_winning = parts[0].strip()
    ticket_numbers = parts[1].strip()
    ticket_numbers = ticket_numbers.split()

    # Further split the Game ID and winning numbers
    game_id, winning_numbers = game_id_and_winning.split(':')
    game_id = game_id.strip()
    winning_numbers = winning_numbers.strip()
    winning_numbers = winning_numbers.split()

    # Extract only the number from the Game ID
    game_id_number = game_id.split()[1]

    return [game_id_number, winning_numbers, ticket_numbers] 

def check_matches(winning_numbers, ticket_numbers):
    # winning_numbers is a list of winning numbers
    # ticket_numbers is a list of ticket numbers
    # Return a list of numbers that match the winning numbers
    matches = []
    for number in ticket_numbers:
        if number in winning_numbers:
            matches.append(number)
    return matches

def calculate_points(matches):
    # Return the number of points
    amount_matches = len(matches)
    points = 2 ** (amount_matches-1)	
    return points

def main04a(file_path):
    # Extract the lines from the file
    lines = extract_lines_from_file(file_path)
    total_points = 0
    # Loop through each line
    for line in lines:
        # Divide the line into 3 parts
        game_id_number, winning_numbers, ticket_numbers = divide_string(line)

        # Check for matches
        matches = check_matches(winning_numbers, ticket_numbers)

        # Calculate the points
        if matches:
            points = calculate_points(matches)
            total_points += points
            # Print the results
            print(f'Game {game_id_number}: {points} points')
        else:
            print(f'Game {game_id_number}: No matches')
    print(f'Total points: {total_points}')

main04a(example_path)
main04a(puzzle_path)