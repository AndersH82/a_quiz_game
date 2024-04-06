import unittest
from unittest.mock import patch
from run import get_non_blank_input, get_yes_no_input


class TestRun(unittest.TestCase):

    @patch('builtins.input', return_value='yes')
    def test_get_yes_no_input_yes(self, mock_input):
        self.assertEqual(get_yes_no_input(
            'Do you wanna read the rules? (yes/no) :'), 'yes')

    @patch('builtins.input', return_value='no')
    def test_get_yes_no_input_no(self, mock_input):
        self.assertEqual(get_yes_no_input(
            'Do you wanna read the rules? (yes/no) :'), 'no')

    @patch('builtins.input', return_value='yes')
    def test_get_yes_no_input(self, input):
        self.assertEqual(get_yes_no_input(
            'Do you want to play? (yes/no): '), 'yes')

    @patch('builtins.input', return_value='john')
    def test_get_non_blank_input(self, input):
        self.assertEqual(get_non_blank_input(
            'Enter your name: '), 'john')


if __name__ == '__main__':
    unittest.main()
