import pandas as pd
from unittest import TestCase
import gcp_pipeline_tests


class TestThisExampleStuff(TestCase):

    def test_length(self):
        
        df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']},
                            index=[0, 1, 2, 3])
        
        
        df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                            'B': ['B4', 'B5', 'B6', 'B7'],
                            'C': ['C4', 'C5', 'C6', 'C7'],
                            'D': ['D4', 'D5', 'D6', 'D7']},
                           index=[4, 5, 6, 7])
        
        result = gcp_pipeline_tests.step_function(df1, df2)
        
        self.assertEqual(len(result), 8)