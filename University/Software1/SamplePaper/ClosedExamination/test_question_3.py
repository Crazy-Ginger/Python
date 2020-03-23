#!/usr/bin/env python3
'''
Created on 8 May 2019

@author: lilia
'''
import unittest
from question_3 import two_out_five

class TestQuestion3(unittest.TestCase):
    def test_valid_input(self):
        """
        Test to check that all digits (0..9) binary representation have been
        converted correctly. Also test that combination of digits is also
        translated properly
        """
        self.assertEqual('0', two_out_five('11000'))
        self.assertEqual('1', two_out_five('00011'))
        self.assertEqual('2', two_out_five('00101'))
        self.assertEqual('3', two_out_five('00110'))
        self.assertEqual('4', two_out_five('01001'))
        self.assertEqual('5', two_out_five('01010'))
        self.assertEqual('6', two_out_five('01100'))
        self.assertEqual('7', two_out_five('10001'))
        self.assertEqual('8', two_out_five('10010'))
        self.assertEqual('9', two_out_five('10100'))
        self.assertEqual('019', two_out_five('110000001110100'))

    def test_type_error(self):
        """
        Test if invalid input type are handled correctly, that is a TypeError
        is raised.
        """
        self.assertRaises(TypeError, two_out_five,[1,1,0,0,0])
        self.assertRaises(TypeError, two_out_five,11000)

    def test_missingbit(self):
        """
        Test if invalid input where bits are missing are handled correctly, that is a ValueError is raised if the size a the message is not a multiple of 5.
        """
        self.assertRaises(ValueError, two_out_five, '110000011')
        self.assertRaises(ValueError, two_out_five, '110000010')

    def test_corruptedbit(self):
        """
        Test if invalid input where the message has too many 1s or 0s is handled correctly, that is a ValueError is raised.
        """
        self.assertRaises(ValueError, two_out_five, '1100000111') #Too many 1s must raise a ValueError!
        self.assertRaises(ValueError, two_out_five, '1100000100') #Too many 0s must raise a ValueError!

if __name__ == "__main__":
    unittest.main()
