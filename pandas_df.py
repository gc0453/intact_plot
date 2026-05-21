import pandas as pd

directory = "data/"
file_name_csv = "activity.csv"
df_csv = pd.read_csv(directory + file_name_csv, sep=',',header=None)
    

