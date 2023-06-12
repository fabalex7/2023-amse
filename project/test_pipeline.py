import pandas as pd
import os.path 
import unittest
import data.data_script


class TestPipeline(unittest.TestCase):
    
    def test_1_whole_pipeline(self):
        
        print("Testing the whole pipeline")
        data.data_script.gather_data()

        self.assertTrue(os.path.exists("./data/my_data.sqlite"))
        
        print("Pipeline test sucessful")
        
        
    def test_2_cyling_data(self):
        
        print("Testing the cycling data loading")
        time_frame = pd.Series(pd.date_range("2020-01-01", "2022-12-31", freq="M"))
        df = data.data_script.read_cycling_data("100035541", time_frame)
        
        self.assertEqual(len(df), 93189)
        
        print("Cycling data test successful")
        
        
    def test_3_rain_data(self):
        
        print("Testing the rain data loading")
        df = data.data_script.read_rain_data("01766")
        
        self.assertEqual(len(df), 157824)
        
        print("Rain data test successful")

if __name__ == "__main__":
    unittest.main()