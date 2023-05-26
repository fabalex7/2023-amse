import pandas as pd
import os.path 
import data.data_script


def test_whole_pipeline():
    
    print("Testing the whole pipeline")
    data.data_script.gather_data()

    if os.path.exists("./data/my_data.sqlite"):
        print("Pipeline test sucessful")
    else:
        print("While testing the pipeline an error occured")
    
    
def test_cyling_data():
    time_frame = pd.Series(pd.date_range("2020-01-01", "2022-12-31", freq="M"))
    df = data.data_script.read_cycling_data("100035541", time_frame)
    print(len(df))

if __name__ == "__main__":
    test_whole_pipeline()
    #test_cyling_data()