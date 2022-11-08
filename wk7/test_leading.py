import unittest
import leading



class TestLeading(unittest.TestCase):
    '''Tests for leading_substrings.'''

    def test_leading_empty(self):
        '''Test an empty string.'''
        output = leading.leading_substrings('')
        output_expected = []
        self.assertEqual(output_expected, output, "The string is empty.")
        
    def test_single_letter(self):
        '''Test one-character  string.'''
        output = leading.leading_substrings('a')
        output_expected = ['a']
        self.assertEqual(output_expected, output, "The string is one character long.")
        
        

if __name__ == '__main__':
    unittest.main()        
     