import unittest
from main02 import check_game, calculate_amount_of_color

class TestCheckGame(unittest.TestCase):
    def test_extract_game_id(self):
        input_line = 'Game 1: 1 green, 2 blue; 13 red, 2 blue, 3 green; 4 green, 14 red'
        expected_output = [1, None]
        result = check_game(10,10,10,input_line)
        self.assertEqual(result[0], expected_output[0])
    def test_check_game_invalid(self):
        input_line = 'Game 1: 1 green, 2 blue; 13 red, 2 blue, 3 green; 4 green, 14 red'
        expected_output = [1, False]
        result = check_game(10,10,10,input_line)
        self.assertEqual(result, expected_output)
    def test_check_game_valid(self):
        input_line = 'Game 1: 1 green, 2 blue; 13 red, 2 blue, 3 green; 4 green, 14 red'
        expected_output = [1, True]
        result = check_game(14,10,10,input_line)
        self.assertEqual(result, expected_output)
    def test_color_green(self):
        input_line = ' 1 green, 2 blue'
        expected_output = 1
        result = calculate_amount_of_color('green',input_line)
        self.assertEqual(result, expected_output)
    def test_color_blue(self):
        input_line = ' 1 green, 21 blue, 5 red'
        expected_output = 21
        result = calculate_amount_of_color('blue',input_line)
        self.assertEqual(result, expected_output)
    def test_color_red(self):
        input_line = ' 1 green, 2 blue, 8 red'
        expected_output = 8
        result = calculate_amount_of_color('red',input_line)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()