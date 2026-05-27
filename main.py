import streamlit as st
from PIL import Image
from analyse import HF_Zonen, Maximum, Umrechnen, HF_Zonen_zeit, avg_power, durchschnittsleistung_pro_zone
from pandas_df import df_csv
from make_plot import bar, plot_line


tab1, tab2 = st.tabs(["Herzfrequenz-Zonen", "Power-Data"]) #Tabs erstellen

zone_times = HF_Zonen_zeit(HF_Zonen(df_csv())) #Daten holen

with tab1:
    st.header("Herzfrequenz-Zonen") #Name Header
    st.write("Zone 1: 50-60% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 1 verbracht: ",Umrechnen(zone_times[0]))
    st.write("durchschnittliche Leistung in Zone 1: ", durchschnittsleistung_pro_zone(df_csv())[1], "Watt")
    st.write("Zone 2: 60-70% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 2 verbracht: ",Umrechnen(zone_times[1]))
    st.write("durchschnittliche Leistung in Zone 2: ", durchschnittsleistung_pro_zone(df_csv())[2], "Watt")
    st.write("Zone 3: 70-80% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 3 verbracht: ",Umrechnen(zone_times[2]))
    st.write("durchschnittliche Leistung in Zone 3: ", durchschnittsleistung_pro_zone(df_csv())[3], "Watt")
    st.write("Zone 4: 80-90% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 4 verbracht: ",Umrechnen(zone_times[3]))
    st.write("durchschnittliche Leistung in Zone 4: ", durchschnittsleistung_pro_zone(df_csv())[4], "Watt")
    st.write("Zone 5: 90-100% der maximalen Herzfrequenz")
    st.write("Zeit in der Zone 5 verbracht: ",Umrechnen(zone_times[4]))
    st.write("durchschnittliche Leistung in Zone 5: ", durchschnittsleistung_pro_zone(df_csv())[5], "Watt")

    st.plotly_chart(bar(zone_times[0], zone_times[1], zone_times[2], zone_times[3], zone_times[4])) #Grafik

with tab2:
    st.header("Power-Data")
    st.write("Maximale Leistung: ", Maximum(df_csv())[0], "Watt, erreicht bei: ", Maximum(df_csv())[1])
    st.write("Durchschnittliche Leistung: ", avg_power(df_csv()), "Watt")

    st.plotly_chart(plot_line(df_csv()))
