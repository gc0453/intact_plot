import pandas as pd


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

    HF_Zone1_time = Umrechnen(len(HF_Zone1))
    HF_Zone2_time = Umrechnen(len(HF_Zone2))
    HF_Zone3_time = Umrechnen(len(HF_Zone3))
    HF_Zone4_time = Umrechnen(len(HF_Zone4))
    HF_Zone5_time = Umrechnen(len(HF_Zone5))


    return HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5, HF_Zone1_time, HF_Zone2_time, HF_Zone3_time, HF_Zone4_time, HF_Zone5_time


def Umrechnen(zeit):
   
    if zeit < 60:
        return zeit
    else:
        minuten = zeit // 60
        sekunden = zeit % 60
        return f"{minuten}:{sekunden} min"
