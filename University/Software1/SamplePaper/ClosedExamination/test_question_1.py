#!/usr/bin/env python3
import unittest
from question_1 import to_barcode

class TestQuestion1(unittest.TestCase):


    def test_to_barcode(self):
        """
        Test to check if you handle normal input correctly, including when 
        inputs are composed solely of 1s or 0s.
        """
        self.assertEqual('..|.|||', to_barcode('0010111'))
        self.assertEqual('..', to_barcode('00'))
        self.assertEqual('||||', to_barcode('1111'))
        
 
    def test_to_barcode_empty_input(self):
        """
        Test to check that you handle correctly an empty word. An empty word 
        results in an empty barcode.
        """
        self.assertEqual('', to_barcode(''))
        

    def test_to_barcode_input_error(self):
        """
        Test to check if you handle invalid inputs properly, that is if the
        word contains symbols other than 1s and 0s a ValueError must be raised
        """
        self.assertIsNone (to_barcode('01120'))


if __name__ == '__main__':
    unittest.main()

