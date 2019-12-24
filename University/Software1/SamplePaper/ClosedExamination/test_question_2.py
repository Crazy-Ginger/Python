'''
Created on 8 May 2019

@author: lilia
'''
import unittest
from question_2 import detect_correct


class TestQuestion2(unittest.TestCase):

    def test_detect_correct(self):
        '''
        Test to check that you handle properly inputs having no errors, at 
        least one error, multiple errors. Also test if the errors have been
        corrected correctly. 
        '''
        self.assertEqual(('010',1), 
                         detect_correct('000111001'), 
                         'Should have detected an error from the last three bits and corrected it to a 0')

        self.assertEqual(('010',0), 
                         detect_correct('000111000'), 
                         'You should not have found an error in the word.')
        
        self.assertEqual(('1101',4), 
                         detect_correct('101110001011'), 
                         'Each three bits word has an error, the number of errors returned should be 4.')
        

    def test_detect_correct_empty_word(self):
        '''
        Test if you handle empty words. An empty word as input should return an empty 
        word as a result with no error detected.
        '''
        self.assertEqual(('',0), 
                         detect_correct(''), 
                         'An empty word should return an empty message with 0 error.')


    def test_detect_correct_input_length_error(self):
        '''
        Test if you handle input with incorrect length properly, that is an
        error is raised if the length is not a multiple of 3.
        '''
        self.assertRaises(ValueError, detect_correct,'01110')


    def test_detect_correct_input_error(self):
        '''
        Test to check if you handle invalid inputs properly, that is if the
        word contains symbols other than 1s and 0s a ValueError is raised
        '''
        self.assertRaises(ValueError, detect_correct,'011200')
        

    def test_detect_correct_input_TypeError(self):
        '''
        Test to check if you handle invalid inputs properly, that is if the
        data type of teh input is not a string a TypeError is raised
        '''
        self.assertRaises(TypeError, detect_correct,[0,1,1,0,0,0])



if __name__ == "__main__":
    unittest.main()