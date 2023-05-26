import os.path 
import data.data_script


data.data_script.gather_data()

if os.path.exists("./data/my_data.sqlite"):
    print("Pipeline test sucessful")
else:
    print("While testing the pipeline an error occured")
    