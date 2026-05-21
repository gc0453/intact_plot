import pandas as pd
from pandas_df import df_csv

def Minimum(data):
    min_Leistung = data['PowerOriginal'].min()
    print(min_Leistung)

def Maximum(data):
    max_Leistung = data['PowerOriginal'].max()
    print(max_Leistung)


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

min_Leistung = Minimum(df_csv())
max_Leistung = Maximum(df_csv())
HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5 = HF_Zonen(df_csv())

print("Zone 1:", HF_Zone1)
#print("Zone 2:", HF_Zone2)
#print("Zone 3:", HF_Zone3)
#print("Zone 4:", HF_Zone4)
#print("Zone 5:", HF_Zone5)



