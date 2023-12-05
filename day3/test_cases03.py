import unittest
from main03 import find_numbers_in_line, check_same_line, check_other_line, check_neighboring_characters

class TestCheckGame(unittest.TestCase):
    def test_random_string01(self):
        input_line = '.50.#.1.2$'
        expected_output = [['50', 1], ['1', 6], ['2', 8]]
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)

    def test_empty_string(self):
        input_line = ''
        expected_output = []
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)

    def test_string_without_numbers(self):
        input_line = '.#.$'
        expected_output = []
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)

    def test_string_with_numbers_only(self):
        input_line = '1234567890'
        expected_output = [['1234567890', 0]]
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)

    def test_string_with_multiple_same_numbers(self):
        input_line = '.1.#.1.1$'
        expected_output = [['1', 1], ['1', 5], ['1', 7]]
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)

    def test_string_with_large_number(self):
        input_line = '.12345678901234567890$'
        expected_output = [['12345678901234567890', 1]]
        result = find_numbers_in_line(input_line)
        self.assertEqual(result, expected_output)
    
    def test_check_same_line(self):
        input_line = '.50#.1.2$'
        input_numbers = [['50', 1], ['1', 5], ['2', 7]]
        expected_output = [[['50', 1], ['2', 7]], [['1', 5]]]
        result = check_same_line(input_line, input_numbers)
        self.assertEqual(result, expected_output)
    def test_other_line(self):
        #...*......
        #..35..633.
        input_line = '...*......'
        input_numbers = [['35', 2], ['633', 6]]
        expected_output = [[['35', 2]], [['633', 6]]]
        result = check_other_line(input_line, input_numbers)
        self.assertEqual(result, expected_output)
    def test_other_line_plussign(self):
        #.....+.58.
        #..592.....
        input_line = '.....+.58.'
        input_numbers = [['592', 2]]
        expected_output = [[['592', 2]], [[]]]
        result = check_other_line(input_line, input_numbers)
        self.assertEqual(result, expected_output)
    def test_neighboring_characters(self):
        #...*......
        #..35..633.
        #......#...
        input_line = ['...*......', '..35..633.', '......#...']
        input_numbers = [['35', 2], ['633', 6]]
        expected_output = [[['35', 2], ['633', 6]], []]
        result = check_neighboring_characters(input_line, input_numbers)
        self.assertEqual(result, expected_output)
    


if __name__ == '__main__':
    unittest.main()