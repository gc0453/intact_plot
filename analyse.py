import pandas as pd
import pandas_df


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
    HF_Zone_5_max= max_Heartrate
    for row in data:
        if HF_Zone_1_min <= data['HeartRate'] < HF_Zone_2_min:
            HF_Zone1.list.append()
        elif HF_Zone_2_min <= data['HeartRate'] < HF_Zone_3_min:
            HF_Zone2.list.append()
        elif HF_Zone_3_min <= data['HeartRate'] < HF_Zone_4_min:
            HF_Zone3.list.append()
        elif HF_Zone_4_min <= data['HeartRate'] < HF_Zone_5_min:
            HF_Zone4.list.append()
        elif HF_Zone_5_min <= data['HeartRate']:
            HF_Zone5.list.append()
    print(HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5)
    #return HF_Zone1, HF_Zone2, HF_Zone3, HF_Zone4, HF_Zone5 



min_Leistung = Minimum(pandas_df.df_csv)
max_Leistung = Maximum(pandas_df.df_csv)
HF_Zone = HF_Zonen(pandas_df.df_csv)



