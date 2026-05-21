import pandas as pd

def df_csv():
    directory = "data/"
    file_name_csv = "activity.csv"
    df = pd.read_csv(directory + file_name_csv, sep=',',header=0)
    df_clean = df.dropna(subset=["PowerOriginal"]) #Alle None aus PowerOriginal entfernen
    df_clean = df.dropna(subset=["HeartRate"]) #Alle None aus HeartRate entfernen
    return print(df_clean)

