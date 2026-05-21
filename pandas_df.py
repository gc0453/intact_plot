import pandas as pd

def df_csv():
    directory = "data/" #Speicherort
    file_name_csv = "activity.csv" #Dateiname der csv-Datei
    df = pd.read_csv(directory + file_name_csv, sep=',',header=0) #Datenframe erstellen
    df_clean = df.dropna(subset=["PowerOriginal"]) #Alle None aus PowerOriginal entfernen
    df_clean = df.dropna(subset=["HeartRate"]) #Alle None aus HeartRate entfernen
    return df_clean #Die "gereinigten" Daten werden zurückgegeben

