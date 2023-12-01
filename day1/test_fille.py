import unittest
from main_01 import extract_pair_from_line

class TestExtractPairFromLine(unittest.TestCase):
    def test_extract_pair_from_line_case1(self):
        input_line = 'ontwonine27'
        expected_output = [2,7]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case2(self):
        input_line = 'fourfivesix78'
        expected_output = [4,8]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case3(self):
        input_line = 'one234five'
        expected_output = [1,5]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case4(self):
        input_line = 'six789zero'
        expected_output = [6,0]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case5(self):
        input_line = 'three456two'
        expected_output = [3,2]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)
    
    def test_extract_pair_from_line_case6(self):
        input_line = 'nonumbershere'
        expected_output = [0, 0]  # No numbers in the string
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case7(self):
        input_line = '1234567890'
        expected_output = [1, 0]  # Only digits, no words
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case8(self):
        input_line = 'onetwothreefourfive'
        expected_output = [1, 5]  # Only words, no digits
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case9(self):
        input_line = ''  # Empty string
        expected_output = [0, 0]
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

    def test_extract_pair_from_line_case10(self):
        input_line = 'one1two2three3four4five5'
        expected_output = [1, 5]  # Mix of words and digits
        result = extract_pair_from_line(input_line)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()