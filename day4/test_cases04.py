import unittest
from main04 import divide_string, check_matches, calculate_points

class TestDivideString(unittest.TestCase):
    def test_case1(self):
        # Test case 1
        # Add your test inputs and expected outputs here
        input_data = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        expected_output = ['1',['41','48','83', '86', '17'],['83','86','6','31','17','9','48','53']]
        self.assertEqual(divide_string(input_data), expected_output)

    def test_case2(self):
        input_data = ['41','48','83', '86', '17']
        input_data2 = ['83','86','6','31','17','9','48','53']
        expected_output = ['83', '86', '17', '48']
        self.assertEqual(check_matches(input_data, input_data2), expected_output)

    # Add more test cases as needed
    def test_case3(self):
        input_data = ['48','83', '17', '86']
        expected_output = 8
        self.assertEqual(calculate_points(input_data), expected_output)
if __name__ == '__main__':
    unittest.main()
