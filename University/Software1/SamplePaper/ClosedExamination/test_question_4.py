#!/usr/bin/env python3
'''
Created on 8 May 2019

@author: lilia
'''
import unittest
from question_4 import import_from_CSV


class TestQuestion4(unittest.TestCase):
    def test_from_CSV_no_dash(self):
        '''
        Test to check if a properly formatted file containing numeric values
        for each data entry is parsed correctly. Make sure that country names 
        and commodities do not have spaces before and after their name. For
        example, it must be 'Canada' not ' Canada', or 'Canada\n' or ' Canada '.
        '''
        self.assertEqual({'Canada': {'Wheat': 27.2, 'Rice Milled': 0.0, 'Oilseeds': 19.0, 'Cotton': 0.0},
                          'USA': {'Wheat': 61.7, 'Cotton': 17.3, 'Rice Milled': 6.3, 'Oilseeds': 93.1}}, 
                         import_from_CSV('data//test_data_nodash.csv'))
 

    def test_from_CSV_with_dash(self):
        '''
        Test to check if a properly formatted file containing numeric values
        for most data entries, with missing information signaled by a - is 
        parsed correctly. Make sure that country names and commodities do not 
        have spaces before and after their name. For example, it must be 
        'Canada' not ' Canada', or 'Canada\n' or ' Canada '.
        '''
        self.assertEqual({'Canada': {'Wheat': 27.2, 'Oilseeds': 19.0},
                          'USA': {'Wheat': 61.7, 'Cotton': 17.3, 'Rice Milled': 6.3, 'Oilseeds': 93.1}}, 
                         import_from_CSV('data//test_data_with_dash.csv'))


    def test_from_CSV_too_many_entries(self):
        '''
        Test if you handle file with an invalid format. In this case you 
        should have detected that there are too many entries on the third line of the file.
        '''
        self.assertRaises(IOError, 
                         import_from_CSV,'data//test_data_too_many_entries.csv')
                         

    def test_from_CSV_missing_entries(self):
        '''
        Test if you handle file with an invalid format. In this case you 
        should have detected that there are missing entries on the third line of the file.'
        '''
        self.assertRaises(IOError, 
                         import_from_CSV,'data//test_data_missing_entries.csv')


if __name__ == "__main__":
    unittest.main()
