import pandas as pd
import numpy as np
from pandas_df import df_csv


def Minimum(data):
    min_Leistung = data['PowerOriginal'].min()
    min_Leistung_zeile = data['PowerOriginal'].idxmin()
    min_Leistung_zeit = Umrechnen(min_Leistung_zeile)
    return(min_Leistung, min_Leistung_zeit)

def Maximum(data):
    max_Leistung = data['PowerOriginal'].max()
    max_Leistung_zeile = data['PowerOriginal'].idxmax()
    max_Leistung_zeit = Umrechnen(max_Leistung_zeile)
    return(max_Leistung, max_Leistung_zeit)


def HF_Zonen(data):
    max_hr = data["HeartRate"].max()

    conditions = [
        data["HeartRate"] < 0.6 * max_hr,
        data["HeartRate"] < 0.7 * max_hr,
        data["HeartRate"] < 0.8 * max_hr,
        data["HeartRate"] < 0.9 * max_hr,
        data["HeartRate"] >= 0.9 * max_hr,
    ]

    choices = [1, 2, 3, 4, 5]

    data["Zone"] = np.select(conditions, choices)

    return data

def HF_Zonen_zeit(data):
    zone_times = []
    for zone in range(1, 6):
        zone_time = len(data[data["Zone"] == zone])
        zone_times.append(zone_time)
    return zone_times

def Umrechnen(zeit):
   
    if zeit < 60:
        sekunden = zeit
        return f"00:{sekunden:02d} min"
    else:
        minuten = zeit // 60
        sekunden = zeit % 60
        return f"{minuten}:{sekunden:02d} min"

def durchschnittsleistung_pro_zone(data):
    zonen_df = HF_Zonen(data)
    avg_power = zonen_df.groupby("Zone")["PowerOriginal"].mean().round(1)
    return avg_power

