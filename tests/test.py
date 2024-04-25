import os
import sys
sys.path.insert(0, '../scripts/')

import unittest
import numpy as np
import pandas as pd


sys.path.append(os.path.abspath(os.path.join('scripts')))
from data_cleaning import DataCleaning
class TestCases(unittest.TestCase):
    def test_fill_missing_values(self):
        # Create a sample DataFrame with missing values
        df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                           'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})
        
        # Create an instance of DataCleaning class
        data_cleaner = DataCleaning(df)
        
        # Specify the value to fill missing values with
        fill_value = 0
        
        # Call the fill_missing_values method
        data_cleaner.fill_missing_values(fill_value)
        
        # Assert that there are no missing values in the cleaned DataFrame
        self.assertFalse(data_cleaner.df.isnull().values.any())
        
        # Assert that the filled values match the specified fill_value
        self.assertTrue((data_cleaner.df == fill_value).all().all())

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
