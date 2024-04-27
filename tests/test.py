import os
import sys
sys.path.insert(0, '../scripts/')

import unittest
import numpy as np
import pandas as pd


sys.path.append(os.path.abspath(os.path.join('scripts')))
from data_cleaning import  convert_to_datetime
import unittest
import pandas as pd

class TestConvertToDatetime(unittest.TestCase):

    def test_convert_to_datetime(self):
        # Create a sample DataFrame
        df = pd.DataFrame({
            'Start': ['2022-04-25', '2022-04-26'],
            'End': ['2022-04-30', '2022-05-01']
        })

        # Call the function
        result_df = convert_to_datetime(df)

        # Check if the 'Start' and 'End' columns are converted to datetime
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result_df['Start']))
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result_df['End']))

        # Check if the output DataFrame has the same shape as the input DataFrame
        self.assertEqual(result_df.shape, df.shape)

        # Check if the output DataFrame has the same index as the input DataFrame
        self.assertTrue(result_df.index.equals(df.index))

        # Check if the output DataFrame has the same values as the input DataFrame
        self.assertTrue(result_df.equals(df))

if __name__ == '__main__':
    unittest.main()

