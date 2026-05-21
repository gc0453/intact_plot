import pandas as pd
from pandas_df import df_csv

def Minimum(data):
    min_Leistung = data['PowerOriginal'].min()
    min_Leistung_zeile = data['PowerOriginal'].idxmin()
    min_Leistung_zeit = min_Leistung_zeile / 60
    return(min_Leistung, min_Leistung_zeit)

def Maximum(data):
    max_Leistung = data['PowerOriginal'].max()
    max_Leistung_zeile = data['PowerOriginal'].idxmax()
    max_Leistung_zeit = max_Leistung_zeile / 60
    return(max_Leistung, max_Leistung_zeit)


def HF_Zonen(data):
    max_Heartrate = data['HeartRate'].max()
    HF_Zone_1_min= max_Heartrate * 0.5
    HF_Zone_2_min= max_Heartrate * 0.6
    HF_Zone_3_min= max_Heartrate * 0.7
    HF_Zone_4_min= max_Heartrate * 0.8
    HF_Zone_5_min= max_Heartrate * 0.9

    HF_Zone1 = []
    HF_Zone2 = []
    HF_Zone3 = []
    HF_Zone4 = []
    HF_Zone5 = []

    for hr in data['HeartRate']:
        if HF_Zone_1_min <= hr < HF_Zone_2_min:
            HF_Zone1.append(hr)
        elif HF_Zone_2_min <= hr < HF_Zone_3_min:
            HF_Zone2.append(hr)
        elif HF_Zone_3_min <= hr < HF_Zone_4_min:
            HF_Zone3.append(hr)
        elif HF_Zone_4_min <= hr < HF_Zone_5_min:
            HF_Zone4.append(hr)
        elif HF_Zone_5_min <= hr:
            HF_Zone5.append(hr)

    return HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5





